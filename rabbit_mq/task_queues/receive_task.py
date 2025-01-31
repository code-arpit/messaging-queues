import os
import sys
import time

import pika


def main():
    # Defining connection and channel
    connection = pika.BlockingConnection(pika.ConnectionParameters("127.0.0.1"))
    channel = connection.channel()

    # Decalaring a queue
    # A Durable queue ensures that id the RabbitMQ server dies or restarts then
    # the queue will remain intact and will not be lost
    channel.queue_declare(queue="task_hello", durable=True)

    # Defining a callback funtion to be called on consumption
    def callback(ch, method, properties, body):
        print(f" [y] received task {body.decode()}")
        time.sleep(body.count(b"."))
        print(" [y] task done")

        # Ensuring the message is acknowledged only on task completion, not before
        # It helps in maintaining reliability on the queue that the task is done
        # if in case a worker dies or crashed.
        ch.basic_ack(delivery_tag=method.delivery_tag)

    # This ensures that the consumer will not be provided with extra tasks
    # until the worker has completed its given task and acknowledged the
    # given task.
    channel.basic_qos(prefetch_count=1)
    # Consuming the tasks and calling the callback function
    channel.basic_consume(queue="task_hello", on_message_callback=callback)

    print(" [*] Waiting for task...... to Exit press CTRL+C")
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
