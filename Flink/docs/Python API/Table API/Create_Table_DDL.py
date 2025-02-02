from pyflink.table import EnvironmentSettings, TableEnvironment

env = EnvironmentSettings.in_streaming_mode()
t_env = TableEnvironment.create(env)

t_env.execute_sql("""
    CREATE TABLE random_source(
        id BIGINT,
        data TINYINT
    ) WITH (
        'connector' = 'datagen',
        'fields.id.kind' = 'sequence',
        'fields.id.start' = '1',
        'fields.id.end' = '3',
        'fields.data.kind' = 'sequence',
        'fields.data.start' = '4',
        'fields.data.end' = '6'
        )
""")

table = t_env.from_path("random_source")
table.execute().print()