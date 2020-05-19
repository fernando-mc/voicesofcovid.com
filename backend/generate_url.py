import boto3
import json
import os
import uuid
import requests
import time

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
GA_SECRET = os.environ['GOOGLE_RECAPTCHA_TOKEN']


def validate_captcha(captcha_response):
    url = 'https://www.google.com/recaptcha/api/siteverify'
    response = json.loads(requests.post(
        url, 
        data={
            'secret': GA_SECRET, 
            'response':captcha_response
        }
    ).text)
    return response['success']


def generate_presigned_url():
    object_name = str(uuid.uuid4())
    response = s3.generate_presigned_post(
        'voicesofcovid',
        object_name,
        Fields={
            "acl": "public-read",
            "content-length-range": [0, 10000000]
        },
        Conditions=[
            {"acl": "public-read"},
            ["content-length-range", 0, 10000000]
        ],
        ExpiresIn=3600
    )
    response = response["fields"]
    del response["content-length-range"]
    return response


def handler(event, context):
    print(event['body'])
    event_body = json.loads(event['body'])
    # Check recaptcha
    try: 
        valid = validate_captcha(event_body['captcha'])
    except Exception:
        valid = False
    if not valid:
        return {
            "statusCode":400,
            "headers": {"Access-Control-Allow-Origin":"*"},
            "body": json.dumps({'status': 'failure', 'message': 'Captcha failed'})
        }
    # Create item in DynamoDB for staging the metadata (before Algolia)
    url_details = generate_presigned_url()
    item = {
        'pk': 'VOICE#ALL',
        'sk': 'VOICE#' + url_details['key'],
        'data': event_body['data']
    }
    table.put_item(Item=item)
    response = {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": json.dumps(url_details)
    }
    return response
