# coding:utf-8

import pika
import sys

__author__ = 'hzliyong'

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue = 'hello', durable = True)

message = ''.join(sys.argv[1:]) or "hello world!"
channel.basic_publish(exchange = '', routing_key = 'hello', body = message, properties = pika.BasicProperties(delivery_mode=2,))
print("[x] Sent %r" % (message, ))
connection.close()
