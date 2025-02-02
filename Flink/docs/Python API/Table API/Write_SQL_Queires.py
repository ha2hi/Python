# SQL 문법은 Apache Calcite 기반
from pyflink.table import EnvironmentSettings, TableEnvironment

env_settings = EnvironmentSettings.in_streaming_mode()
t_env = TableEnvironment.create(env_settings)

t_env.execute_sql("""
    CREATE TABLE random_source(
        id BIGINT,
        data TINYINT
    ) WITH (
        'connector' = 'datagen',
        'fields.id.kind' = 'sequence',
        'fields.id.start' = '1',
        'fields.id.end' = '8',
        'fields.data.kind' = 'sequence',
        'fields.data.start' = '4',
        'fields.data.end' = '11'
    )
""")

t_env.execute_sql("""
    CREATE TABLE print_sink(
        id BIGINT,
        data TINYINT    
    ) WITH (
        'connector' = 'print'
    )
""")

t_env.execute_sql("""
    INSERT INTO print_sink
        SELECT id, sum(data) as data_sum FROM
            (SELECT id / 2 as id, data FROM random_source)
        WHERE id > 1
        GROUP BY id
""").wait()