from kafka import KafkaConsumer, KafkaProducer
import json
PAYMENT_TOPIC = "payments"
FRAUD_TOPIC = "fraud_payments"
LEGIT_TOPIC = "legit_payments"

brokers = ['localhost:9091', 'localhost:9092', 'localhost:9093']

consumer = KafkaConsumer(PAYMENT_TOPIC, bootstrap_servers=brokers)
producer = KafkaProducer(bootstrap_servers=brokers)

def is_suspicious(transactions):
    if transactions['PAYMENT_TYPE'] == 'BITCOIN':
        return True
    return False


for message in consumer:
    msg = json.load(message.value.decode())
    print(msg['PAYMENT_TYPE'])

    topic = FRAUD_TOPIC if is_suspicious(msg) else LEGIT_TOPIC

    producer.send(topic, json.dumps(msg).encode('utf-8'))