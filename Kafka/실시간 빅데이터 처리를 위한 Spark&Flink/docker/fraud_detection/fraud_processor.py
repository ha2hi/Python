from kafka import KafkaConsumer
import json


brokers = ['localhost:9091', 'localhost:9092', 'localhost:9093']
FRAUD_TOPIC = 'fraud_payments'

consumer = KafkaConsumer(FRAUD_TOPIC, bootstrap_servers = brokers)

for message in consumer:
    msg = json.loads(message.value.decode())
    if msg['TO'] == 'stranger':
        print('[ALERT] fraud ditector')
    else:
        to = msg['TO']
        amount = msg['AMOUNT']
        print(f'[PROCESSING BITCOIN] {to} - {amount}')