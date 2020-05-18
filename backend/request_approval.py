import boto3
import json

ses = boto3.client('ses')

APPROVE_API_ENDPOINT = "https://8h8vhvd4te.execute-api.us-east-1.amazonaws.com/dev/approve/"
# Make sure to verify these emails in SES first
FROM_ADDRESS = 'fernandomc.sea@gmail.com'
REPLY_TO_ADDRESS = FROM_ADDRESS
ADMIN_ADDRESS = 'fmcorey@gmail.com'


def handler(event, context):
    s3_key = event['Records'][0]['s3']['object']['key']
    public_link = "https://voicesofcovid.s3.amazonaws.com/" + s3_key
    approve_link = APPROVE_API_ENDPOINT + s3_key
    message = (
        'A new submission can be seen here: ' + public_link + 
        '\n\n To approve, please use: ' + approve_link
    )
    ses.send_email(
        Source=FROM_ADDRESS,
        Destination={
            'ToAddresses': [ADMIN_ADDRESS],
            'CcAddresses': [],
            'BccAddresses': []
        },
        Message={
            'Subject': {
                'Data': 'A new submission needs approval',
            },
            'Body': {
                'Text': {
                    'Data': message
                }
            }
        },
        ReplyToAddresses=[
            REPLY_TO_ADDRESS,
        ]
    )
    response = {
        "statusCode": 200,
        "body": json.dumps(public_link)
    }
    return response