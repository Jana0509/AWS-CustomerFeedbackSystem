import json
import boto3
from botocore.exceptions import ClientError

# Initialize a DynamoDB client
dynamo_client = boto3.resource('dynamodb')
table = dynamo_client.Table('CustomerFeedback')

def lambda_handler(event, context):
    try:
        # Parse the incoming event to get userId and feedback
        body = json.loads(event['body'])
        user_id = body.get('userId')  # Use .get() to avoid KeyError
        user_feedback = body.get('feedback')

        # Validate required fields
        if not user_id or not user_feedback:
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'userId and feedback are required in the request body'})
            }
        
        # Insert data into DynamoDB
        table.put_item(
            Item={
                'userID': user_id,
                'feedback': user_feedback
            }
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'User feedback inserted successfully'})
        }

    except json.JSONDecodeError:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Invalid JSON in request body'})
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Failed to insert feedback', 'error': str(e)})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'An unexpected error occurred', 'error': str(e)})
        }
