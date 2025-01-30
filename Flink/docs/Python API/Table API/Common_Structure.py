from pyflink.table import EnvironmentSettings, TableEnvironment
from pyflink.table.expressions import col

env = EnvironmentSettings.in_streaming_mode()
t_env = TableEnvironment.create(env)

t_env.execute_sql("""
    CREATE TABLE datagen(
        id INT,
        data STRING
    ) WITH(
        'connector' = 'datagen',
        'fields.id.kind' = 'sequence',
        'fields.id.start' = '1',
        'fields.id.end' = '10'
        )
""")

t_env.execute_sql("""
    CREATE TABLE print (
        id INT,
        data STRING
    ) WITH(
        'connector' = 'print'
        )
""")

source_table = t_env.from_path("datagen")
# source_table = t_env.sql_query("SELECT * FROM datagen")

result_table = source_table.select(col("id") + 1, col("data"))
# result_table = t_env.sql_query("SELECT id+1, data FROM datagen")

result_table.execute_insert("print").wait()
# t_env.execute_sql("INSERT INTO print SELECT * FROM datagen").wait()