import boto3
import json
import os
import requests
import time
import uuid

from algoliasearch.search_client import SearchClient

ALGOLIA_APPLICATION_ID = os.environ['ALGOLIA_APPLICATION_ID']
ALGOLIA_ADMIN_API_KEY = os.environ['ALGOLIA_ADMIN_API_KEY']
client = SearchClient.create(
    ALGOLIA_APPLICATION_ID,
    ALGOLIA_ADMIN_API_KEY
)
ag_index = client.init_index('voicesofcovid')

DYNAMODB_TABLE = os.environ['DYNAMODB_TABLE']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(DYNAMODB_TABLE)


def handler(event, context):
    s3_key = event['pathParameters']['id']
    data = table.get_item(
        Key={
            'pk': 'VOICE#ALL',
            'sk': 'VOICE#' + s3_key
        }
    )['Item']['data']
    data['id'] = s3_key
    data['url'] = 'https://voicesofcovid.s3.amazonaws.com/' + s3_key
    data['objectID'] = s3_key
    ag_index.save_object(data)
    return {
        "statusCode":200,
        "headers": {"Access-Control-Allow-Origin":"*"},
        "body": json.dumps(data)
    }
