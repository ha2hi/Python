from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import StreamTableEnvironment
from pyflink.common.typeinfo import Types

env = StreamExecutionEnvironment.get_execution_environment()
t_env = StreamTableEnvironment.create(env)

# create a DataStream
ds = env.from_collection(["Alice", "Bob", "John"], Types.STRING())

t = t_env.from_data_stream(ds)
t_env.create_temporary_view("InputTable", t)
res_table = t_env.sql_query("SELECT UPPER(f0) FROM InputTable")

res_ds = t_env.to_data_stream(res_table)

res_ds.print()

env.execute()