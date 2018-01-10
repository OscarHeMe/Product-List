#!/usr/bin/env python

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel    = connection.channel()

#Declaring the queue to consume
channel.queue_declare(queue='hello')

#declaring the exchange, routing_key='name of queue'
channel.basic_publish(exchange='', 
                      routing_key='hello',
                      body='Hello Moto')
print(" [x] Sent message")
connection.close()




