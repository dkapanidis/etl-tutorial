import boto3

# Create SQS client
sqs = boto3.client('sqs')

def sqs_receive_message(queue_url: str) -> list:
    # Receive message from SQS queue
    response = sqs.receive_message(
        QueueUrl=queue_url,
        AttributeNames=[
            'SentTimestamp'
        ],
        MaxNumberOfMessages=1,
        MessageAttributeNames=[
            'All'
        ],
        VisibilityTimeout=0,
        WaitTimeSeconds=0
    )
    
    if 'Messages' in response:
        return response["Messages"]
    return []

def sqs_delete_message(queue_url: str, receipt_handle: str):
    return sqs.delete_message(
         QueueUrl=queue_url,
         ReceiptHandle=receipt_handle
     )
