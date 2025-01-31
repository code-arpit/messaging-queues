import boto3

# Receive Messages
## More on : 'https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/client/receive_message.html'

# Create SQS client
sqs = boto3.client(
    "sqs",
    aws_access_key_id="<access_key>",
    aws_secret_access_key="<secret_access_key>",
    region_name="<region_name>",
)

queue_url = "<queue_url>"

while True:
    # Receive message from SQS queue
    response = sqs.receive_message(
        QueueUrl=queue_url,
        AttributeNames=["SentTimestamp"],
        MaxNumberOfMessages=1,
        MessageAttributeNames=["All"],
        VisibilityTimeout=0,
        WaitTimeSeconds=0,
    )
    if not "Messages" in response:
        break
    print(
        response["Messages"][0]["MessageId"], "----->", response["Messages"][0]["Body"]
    )
    sqs.delete_message(
        QueueUrl=queue_url, ReceiptHandle=response["Messages"][0]["ReceiptHandle"]
    )
