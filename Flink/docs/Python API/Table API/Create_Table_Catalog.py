from pyflink.table import EnvironmentSettings, TableEnvironment

env = EnvironmentSettings.in_streaming_mode()
t_env = TableEnvironment.create(env)

table = t_env.from_elements([(1, 'Hi'), (2, 'Hello')], ['id', 'data'])
t_env.create_temporary_view('source_table', table)

new_table = t_env.from_path('source_table')
new_table.execute().print()