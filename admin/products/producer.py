import pika, json

params = pika.URLParameters('AMQP URL')

connections = pika.BlockingConnection(params)

channel = connections.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
