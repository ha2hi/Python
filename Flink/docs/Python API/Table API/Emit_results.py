from pyflink.table import EnvironmentSettings, TableEnvironment

env = EnvironmentSettings.in_streaming_mode()
t_env = TableEnvironment.create(env)

source = t_env.from_elements([(1, "Hi", "Hello"), (2, "Hello", "Hello")], ["a", "b", "c"])
source.execute().print()

# Collect Results to Client #
table_result = t_env.execute_sql("select a + 1, b, c from %s" % source)
with table_result.collect() as results:
    for result in results:
        print(result)

# Collect Results to Client by converting it to pandas DataFrame #
print(source.to_pandas())

# Emit Results to One Sink Table #
t_env.execute_sql("""
    CREATE TABLE sink (
        a BIGINT,
        b STRING,
        c STRING
    ) WITH (
        'connector' = 'print')
""")

source.execute_insert("sink").wait()