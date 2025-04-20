#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Declare multiple queues
print(":::  creating sms queue  :::")

channel.queue_declare(queue='sms')
print(":::  creating email queue  :::")

channel.queue_declare(queue='email')
print(":::  creating pdf queue  :::")

channel.queue_declare(queue='pdf')

# while True:
#     message = input("message : ")
#     if message=="q":
#         connection.close()
#         break
#     channel.basic_publish(exchange='', routing_key='email', body=message)


def send_message(queue_name, message_body):
    channel.basic_publish(exchange='', routing_key=queue_name, body=message)



while True:
    queue_name = input("queue name : ")
    message = input("message body: ")

    if message=="q":
        connection.close()
        break
    send_message(queue_name, message)

