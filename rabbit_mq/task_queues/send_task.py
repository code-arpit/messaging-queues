import sys

import pika

# Making a connection with the rabbitmq server and defining a channel
connection = pika.BlockingConnection(pika.ConnectionParameters("127.0.0.1"))
channel = connection.channel()

# Declaring a queue as durable so that if the RabbitMQ server restarts then
# the queue will not be lost.
channel.queue_declare(queue="task_hello", durable=True)

message = " ".join(sys.argv[1:]) or "Hello World Task"
channel.basic_publish(
    exchange="",
    routing_key="task_hello",
    body=message,
    properties=pika.BasicProperties(delivery_mode=pika.DeliveryMode.Persistent),
)
print(f" [x] sent! {message}")
