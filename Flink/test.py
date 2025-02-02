from pyflink.table import EnvironmentSettings, TableEnvironment

env = EnvironmentSettings.in_streaming_mode()
table_env = TableEnvironment.create(env)

source = table_env.from_elements([(1, "Hi", "Hello"), (2, "Hello", "Hello")], ["a", "b", "c"])

# Get TableResult
table_result = table_env.sql_query("select a + 1, b, c from %s" % source)

# Print the table
table_result.execute().wait()