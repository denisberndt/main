#amqps://lrrgthdt:NSDs4G-ylgdC1rvBZEXUI2pHvH5cZ32N@cow.rmq2.cloudamqp.com/lrrgthdt

import pika, json

params = pika.URLParameters('amqps://lrrgthdt:6bnDhGqcywL-WKJbe5rN0yagP2BNio1V@cow.rmq2.cloudamqp.com/lrrgthdt')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)