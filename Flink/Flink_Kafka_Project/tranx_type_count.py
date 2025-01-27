import os
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors.kafka import FlinkKafkaProducer, FlinkKafkaConsumer
from pyflink.datastream.formats.avro import AvroRowSerializationSchema, AvroRowDeserializationSchema
from pyflink.table import StreamTableEnvironment, EnvironmentSettings, DataTypes
from pyflink.table.udf import udf

env = StreamExecutionEnvironment.get_execution_environment()
env.set_parallelism(1)
t_env = StreamTableEnvironment.create(env, environment_settings = EnvironmentSettings.in_streaming_mode())

env.add_jars("file:///root/flink-sql-connector-kafka-3.3.0-1.20.jar",
             "file:///root/flink-sql-avro-confluent-registry-1.20.0.jar")

deserialization_schema = AvroRowDeserializationSchema(
    avro_schema_string="""
        {
        "namespace": "tranx.avro",
        "type": "record",
        "name": "TransactionRecord",
        "fields": [
                {"name": "ID", "type": "string"},
                {"name": "TRANSACTION_TYPE",  "type": "string"},
                {"name": "AMOUNT", "type": "int"},
                {"name": "DATE_MS", "type": "long"},
                {"name": "CURRENCY", "type": "string"}
            ]
        }"""
)

kafka_consumer = FlinkKafkaConsumer(
    topics='transaction',
    deserialization_schema=deserialization_schema,
    properties={'bootstrap.servers': 'localhost:9092', 'group.id': 'test_group_1'}
)
kafka_consumer.set_start_from_earliest()

env.add_source(kafka_consumer).print()
env.execute()