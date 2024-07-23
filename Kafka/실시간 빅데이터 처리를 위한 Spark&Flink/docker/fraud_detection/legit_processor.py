from kafka import KafkaConsumer
import json

brokers = ['localhost:9091', 'localhost:9092', 'localhost:9093']
LEGIT_TOPIC = 'legit_payments'

consumer = KafkaConsumer(LEGIT_TOPIC, bootstrap_servers = brokers)

for message in consumer:
    msg = json.loads(message.value.decode())
    if msg['PAYMENT_TYPE'] == 'VISA':
        print('VISA')
    elif msg['PAYMENT_TYPE'] == 'MASTERCARD':
        print('MASTERCARD')
    else:
        print('[ALERT] unable to process payments')