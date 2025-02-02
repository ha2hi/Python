# 여러 Sink에 저장하려는 경우 statement를 사용하여 insert
from pyflink.table import EnvironmentSettings, TableEnvironment

env = EnvironmentSettings.in_streaming_mode()
t_env = TableEnvironment.create(env)

table = t_env.from_elements([(1, "Hi"), (2, "Hello")], ["id", "data"])
t_env.create_temporary_view("simple_source", table)

t_env.execute_sql("""
    CREATE TABLE first_sink_table (
        id BIGINT, 
        data VARCHAR 
    ) WITH (
        'connector' = 'print'
    )
""")

t_env.execute_sql("""
    CREATE TABLE second_sink_table (
        id BIGINT, 
        data VARCHAR
    ) WITH (
        'connector' = 'print'
    )
""")

statement_set = t_env.create_statement_set()

statement_set.add_insert("first_sink_table", table)
statement_set.add_insert("second_sink_table", table)

# statement_set.add_insert_sql("INSET INTO first_sink_table SELECT * FROM simple_source")
# statement_set.add_insert_sql("INSET INTO second_sink_table SELECT * FROM simple_source")

statement_set.execute().wait()