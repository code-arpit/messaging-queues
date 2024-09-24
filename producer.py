import boto3

# Create SQS client
sqs = boto3.client('sqs',
            aws_access_key_id='<access_key>',
            aws_secret_access_key='<secret_access_key>',
            region_name='<region>'
        )

queue_url = '<queue_url>'

# Send message to SQS queue
for i in range(20):
    response = sqs.send_message(
        QueueUrl=queue_url,
        DelaySeconds=10,
        MessageBody=(str(i))
    )

    print(response['MessageId'])

