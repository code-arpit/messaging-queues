import os
import sys

import pika


def main():
    # Making connection to rabbit mq host
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="127.0.0.1"))
    channel = connection.channel()

    # Defining a queue to listen to
    channel.queue_declare("hello")

    # Defining a callback function of recevining messages
    def callback(ch, method, properties, body):
        print("method", method, "\n\n")
        print("properties", properties.__dict__, "\n\n")
        print(f" [y] Received {body} ")

    # consuming messages
    channel.basic_consume(queue="hello", on_message_callback=callback, auto_ack=True)

    print(" [*]  Waiting for messages. To Exit press CTRL+C")
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("User Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
