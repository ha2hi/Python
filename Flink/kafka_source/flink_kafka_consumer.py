import os
from pyflink.common.serialization import SimpleStringSchema
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors import FlinkKafkaConsumer
from pyflink.datastream.execution_mode import RuntimeExecutionMode 
from pyflink.table import StreamTableEnvironment

env = StreamExecutionEnvironment.get_execution_environment()
env.set_runtime_mode(execution_mode = RuntimeExecutionMode.STREAMING)
env.enable_checkpointing(1000)
env.get_checkpoint_config().set_max_concurrent_checkpoints(1)

t_env = StreamTableEnvironment.create(env)

kafka_jar_path = os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    'flink-sql-connector-kafka-3.4.0-1.20.jar'
)

t_env.get_config().get_configuration().set_string(
    "pipeline.jars", f"file://{kafka_jar_path}"
)

schema = SimpleStringSchema()
