# coding:utf-8
import pika
import time
__author__ = 'hzliyong'

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')

'''exchange为空字符串，可以允许发送给制定的queue，routing_key就是制定的queue名字'''
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')


def send():
    for i in range(10):
        time.sleep(2)
        channel.basic_publish(exchange='', routing_key='hello', body='Hello World!' + str(i))
send()

print("[x] Sent 'Hello World!'")
connection.close()
