import os
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import StreamTableEnvironment, EnvironmentSettings, DataTypes
from pyflink.table.udf import udf

env = StreamExecutionEnvironment.get_execution_environment()
env.set_parallelism(1)
t_env = StreamTableEnvironment.create(env, environment_settings = EnvironmentSettings.in_streaming_mode())

kafka_jar_path = os.path.join(
  os.path.abspath(os.path.dirname(__file__)), "../",
  "flink-sql-connector-kafka-3.3.0-1.20.jar"
)
avro_jar_path = os.path.join(
  os.path.abspath(os.path.dirname(__file__)), "../",
  "flink-sql-avro-1.14.4.jar"
)

t_env.get_config().set("pipeline.jars", "file:///root/flink-sql-connector-kafka-3.3.0-1.20.jar")
t_env.get_config().set("pipeline.jars", "file:///root/flink-sql-avro-1.14.4.jar")

source_query = """
    CREATE TABLE transaction (
        ID STRING,
        TRANSACTION_TYPE STRING,
        AMOUNT BIGINT,
        DATE_MS BIGINT,
        CURRENCY STRING,
        TS AS TO_TIMESTAMP_LTZ(DATE_MS, 3),
        WATERMARK FOR TS AS TS - INTERVAL '5' SECOND
    ) WITH(
      'connector' = 'kafka',
      'topic' = 'transaction',
      'properties.bootstrap.servers' = 'localhost:9092',
      'properties.group.id' = 'trax-group',
      'format' = 'json',
      'scan.startup.mode' = 'latest-offset'
      )
"""

sink_query = """
  CREATE TABLE sink(
        ID STRING,
        TRANSACTION_TYPE STRING,
        AMOUNT BIGINT,
        DATE_MS BIGINT,
        CURRENCY STRING,
        TS TIMESTAMP_LTZ
  ) WITH(
    'connector' = 'print'
  )
"""


t_env.execute_sql(source_query)
t_env.execute_sql(sink_query)

# t_env.from_path("transaction").insert_into("sink").wait()
data = t_env.sql_query("""
SELECT
  *
FROM
  transaction
""")
print(data.to_pandas())