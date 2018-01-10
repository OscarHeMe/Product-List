#!/usr/bin/env python

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel    = connection.channel()

# Declaring the queue to consume
channel.queue_declare(queue='task_queue', durable=True)

# Declaring the exchange type
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

message    = ' '.join(sys.argv[1:]) or "Hello World!"

# Declaring the exchange, routing_key='name of queue'
channel.basic_publish(exchange='logs', 
                      routing_key='task_',
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))
print(" [x] Sent %r" % message)
connection.close()




