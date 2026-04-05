import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('InventoryTable')

def lambda_handler(event, context):

    response = table.scan()

    products = response['Items']

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(products)
    }