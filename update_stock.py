import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('InventoryTable')

def lambda_handler(event, context):

    body = json.loads(event['body'])

    table.update_item(
        Key={
            "product_id": body["product_id"]
        },
        UpdateExpression="set stock = :s",
        ExpressionAttributeValues={
            ":s": int(body["stock"])
        }
    )

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps({"message": "Stock updated"})
    }