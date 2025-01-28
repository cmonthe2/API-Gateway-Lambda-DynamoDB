import json
import boto3
import os

# Initialize DynamoDB client
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["TABLE_NAME"])

def lambda_handler(event, context):
    try:
        http_method = event["requestContext"]["http"]["method"]

        if http_method == "POST":
            return create_user(event)
        elif http_method == "GET":
            return get_user(event)
        elif http_method == "PUT":
            return update_user(event)
        elif http_method == "DELETE":
            return delete_user(event)
        else:
            return response(400, {"message": "Unsupported HTTP method"})

    except Exception as e:
        return response(500, {"error": str(e)})

def create_user(event):
    body = json.loads(event["body"])
    table.put_item(Item=body)
    return response(200, {"message": "User created successfully"})

def get_user(event):
    user_id = event["queryStringParameters"]["UserId"]
    result = table.get_item(Key={"UserId": user_id})
    return response(200, result.get("Item", {}))

def update_user(event):
    body = json.loads(event["body"])
    table.put_item(Item=body)
    return response(200, {"message": "User updated successfully"})

def delete_user(event):
    user_id = event["queryStringParameters"]["UserId"]
    table.delete_item(Key={"UserId": user_id})
    return response(200, {"message": "User deleted successfully"})

def response(status_code, body):
    return {
        "statusCode": status_code,
        "body": json.dumps(body),
        "headers": {"Content-Type": "application/json"}
    }
