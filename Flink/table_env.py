from pyflink.table import EnvironmentSettings, TableEnvironment 

# Create Batch Table Env
batch_settings = EnvironmentSettings.in_batch_mode()
batch_table_env = TableEnvironment.create(batch_settings)

# Create Stream Table Env
stream_settings = EnvironmentSettings.in_streaming_mode()
stream_table_env = TableEnvironment.create(stream_settings)