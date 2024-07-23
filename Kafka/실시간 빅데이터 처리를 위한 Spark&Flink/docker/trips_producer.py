# parquet to Stream
from kafka import KafkaProducer
import csv
import json
import time

brokers = ['localhost:9091', 'localhost:9092', 'localhost:9093']
producer = KafkaProducer(bootstrap_server=brokers)

with open("./trips/yellow_tripdata_2021-01.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        producer.send("trips", json.dumps(row).encode('utf-8'))
        print(row)

        time.sleep(1)