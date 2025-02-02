# Table을 DataStream으로 변환할 때 to_data_stream(append-only)을 사용하는 경우 업데이트 처리는 불가능하다.
# to_changelog_stream을 사용해야됨.
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import StreamTableEnvironment
from pyflink.common.typeinfo import Types

env = StreamExecutionEnvironment.get_execution_environment()
t_env = StreamTableEnvironment.create(env)

ds = env.from_collection([("Alice", 12), ("Bob", 10), ("Alice", 100)],
                        type_info = Types.ROW_NAMED(
                        ["a", "b"],
                        [Types.STRING(), Types.INT()]))

input_table = t_env.from_data_stream(ds).alias("name", "score")

t_env.create_temporary_view("InputTable", input_table)
res_table = t_env.sql_query("SELECT name, SUM(score) FROM InputTable GROUP BY name")

res_stream = t_env.to_changelog_stream(res_table)

res_stream.print()
env.execute()