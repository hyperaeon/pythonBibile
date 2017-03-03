# coding:utf-8

import pika
import time

__author__ = 'hzliyong'


def callback(ch, method, properties, body):
    s = str(body)
    print("[x] Received %r" %(s,))
    i = s.count(' ')
    time.sleep(i)
    print(' [x] Done')
    ch.basic_ack(delivery_tag = method.delivery_tag)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue = 'hello', durable=True)

channel.basic_consume(callback, queue = 'hello')
print('[*] Waiting for message. To exit press CTRL+C')
channel.start_consuming()
