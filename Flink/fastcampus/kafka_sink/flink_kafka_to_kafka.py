import os
from pyflink.common.serialization import SimpleStringSchema
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors import FlinkKafkaConsumer, FlinkKafkaProducer
from pyflink.datastream.execution_mode import RuntimeExecutionMode 

env = StreamExecutionEnvironment.get_execution_environment()
env.set_runtime_mode(execution_mode = RuntimeExecutionMode.STREAMING)
env.enable_checkpointing(1000)
env.get_checkpoint_config().set_max_concurrent_checkpoints(1)

t_env = StreamTableEnvironment.create(env)

kafka_jar_path = os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    'flink-connector-kafka-3.4.0-1.20.jar'
)

t_env.get_config().get_configuration().set_string(
  "pipeline.jars", f"file://{kafka_jar_path}"
)

in_schema = SimpleStringSchema()
kafka_consumer = FlinkKafkaConsumer(
  topics="example-source",
  deserialization_schema=in_schema,
  properties={
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'test_group'
  })

out_schema = SimpleStringSchema()
kafka_producer = FlinkKafkaProducer(
  topics="example-destination",
  deserialization_schema=out_schema,
  properties={
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'test_group'
  })

ds = t_env.add_source(kafka_consumer)
ds.add_sink(kafka_producer)