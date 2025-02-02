from pyflink.datastream import StreamExecutionEnvironment, RuntimeExecutionMode
from pyflink.table import StreamTableEnvironment, EnvironmentSettings

# 방법 1
env = StreamExecutionEnvironment.get_execution_environment()
env.set_runtime_mode(RuntimeExecutionMode.BATCH)
t_env = StreamTableEnvironment.create(env)

# 방법 2
env = StreamExecutionEnvironment.get_execution_environment()
t_env = StreamTableEnvironment.create(env, EnvironmentSettings.in_batch_mode())
