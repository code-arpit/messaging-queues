import boto3

# Create a boto3 sqs client
client = boto3.client(
    "sqs",
    aws_access_key_id="<access_key>",
    aws_secret_access_key="<secret_access_key>",
    region_name="<region_name>",
)

# Create a queue
## More on : 'https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/client/create_queue.html'
response = client.create_queue(
    QueueName="string", Attributes={"string": "string"}, tags={"string": "string"}
)

# List queues
## More on : 'https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/client/list_queues.html'
response = client.list_queues()

# Delete Messages
## More on : 'https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/client/delete_message.html'

response = client.delete_message(QueueUrl="string", ReceiptHandle="string")
