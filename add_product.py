import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('InventoryTable')

def lambda_handler(event, context):

    body = json.loads(event['body'])

    product_id = str(uuid.uuid4())

    table.put_item(
        Item={
            "product_id": product_id,
            "product_name": body["product_name"],
            "category": body["category"],
            "price": int(body["price"]),
            "stock": int(body["stock"]),
            "threshold": int(body["threshold"])
        }
    )

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps({"message": "Product added successfully"})
    }