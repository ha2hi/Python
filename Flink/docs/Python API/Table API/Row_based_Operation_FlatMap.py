from pyflink.common import Row
from pyflink.table.udf import udtf
from pyflink.table import EnvironmentSettings, TableEnvironment

set_settings = EnvironmentSettings.in_batch_mode()
t_env = TableEnvironment.create(set_settings)

table = t_env.from_elements([(1, 'Hi,Flink'), (2, 'Hello')], ['id', 'data'])

@udtf(result_types = ['INT', 'STRING'])
def split(x: Row) -> Row:
    for s in x.data.split(","):
        yield x.id, s

table.flat_map(split).execute().print()

table.join_lateral(split.alias('a', 'b')).execute().print()