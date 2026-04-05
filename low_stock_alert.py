import boto3

dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')

table = dynamodb.Table('InventoryTable')

TOPIC_ARN = "YOUR_SNS_TOPIC_ARN"

def lambda_handler(event, context):

    response = table.scan()

    for item in response['Items']:

        if item['stock'] < item['threshold']:

            sns.publish(
                TopicArn=TOPIC_ARN,
                Subject="Low Stock Alert",
                Message=f"{item['product_name']} stock is low: {item['stock']}"
            )

    return {
        "statusCode": 200,
        "body": "Stock check completed"
    }