import boto3
import json
import os
import requests
import time
import uuid

from algoliasearch import algoliasearch

GA_SECRET = os.environ['GOOGLE_RECAPTCHA_TOKEN']

ALGOLIA_APPLICATION_ID = os.environ['ALGOLIA_APPLICATION_ID']
ALGOLIA_ADMIN_API_KEY = os.environ['ALGOLIA_ADMIN_API_KEY']
client = algoliasearch.Client(
    ALGOLIA_APPLICATION_ID, 
    ALGOLIA_ADMIN_API_KEY
)
ag_index = client.init_index('voicesofcovid')

DYNAMODB_TABLE = os.environ['DYNAMODB_TABLE']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(DYNAMODB_TABLE)


def handler(event, context):
    print(event['body'])
    event_body = event['body']
    if not validate_captcha(str(event_body['captcha'])):
        return {
            "statusCode":400,
            "headers": {"Access-Control-Allow-Origin":"*"},
            "body": {'status': 'failure', 'message': 'Captcha failed'}
        }
    data = event_body['data']
    data['epochtimestamp'] = int(time.time() * 1000)
    data['date'] = time.strftime('%b %d, %Y')
    data['submission_id'] = str(uuid.uuid4())
    data['pk'] = "VOICE#ALL"
    data['sk'] = "VOICE#" + data['submission_id']
    result = table.put_item(Item=data)
    ag_index.add_object(item)
    return {
        "statusCode":200,
        "headers": {"Access-Control-Allow-Origin":"*"},
        "body": data
    }


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
