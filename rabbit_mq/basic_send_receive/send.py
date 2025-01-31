import pika

# Making connection via ip to rabbit MQ broker
connection = pika.BlockingConnection(pika.ConnectionParameters("127.0.0.1"))
channel = connection.channel()


# Creating a rabbit mq queue
channel.queue_declare(queue="hello")

# Sending a message in the queue
channel.basic_publish(exchange="", routing_key="hello", body="hello worldy")
print(" [x] Sent 'Hello Worldy' ")

connection.close()
