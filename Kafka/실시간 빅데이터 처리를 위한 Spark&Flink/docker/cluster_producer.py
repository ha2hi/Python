from kafka import KafkaProducer

brokers = ['15.164.217.126:9094', '15.164.217.126:9095', '15.164.217.126:9096']
topicName = 'first-cluster-topic'

producer = KafkaProducer(bootstrap_servers = brokers)

producer.send(topicName, b"Hello Kafka World")

producer.flush()
