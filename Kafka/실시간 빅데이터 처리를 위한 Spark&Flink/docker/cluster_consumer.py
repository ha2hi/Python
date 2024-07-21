from kafka import KafkaConsumer

brokers = ['15.164.217.126:9091', '15.164.217.126:9092', '15.164.217.126:9093']
topicName = 'first-cluster-topic'

consumer = KafkaConsumer(topicName, bootstrap_servers=brokers)

for message in consumer:
    print(message)