#!/usr/bin/env python

import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel    = connection.channel()

channel.queue_declare(queue='task_', durable=True)

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag) # return an acknowledge message

# Sets rabbitmq not to give more than 1 message to a busy worker
channel.basic_qos(prefetch_count=1)

channel.basic_consume(callback,
                      queue='task_queue',
                      no_ack=False)

print(' [*] Waiting for messages. To exit press CTRL+C')
#Infinite loop waiting for callbacks
channel.start_consuming()


