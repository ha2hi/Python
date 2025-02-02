from pyflink.common import Row
from pyflink.table import EnvironmentSettings, TableEnvironment
from pyflink.table.expressions import col
from pyflink.table.udf import udf
import pandas as pd

env_settings = EnvironmentSettings.in_batch_mode()
t_env = TableEnvironment.create(env_settings)

table = t_env.from_elements([(1, 'Hi'), (2, 'Hello')], ['id', 'data'])

@udf(result_type = 'ROW<id BIGINT, data STRING>')
def func1(id, data) -> Row:
    return Row(id, data*2)

table.map(func1(col('id'), col('data'))).execute().print()

@udf(result_type = 'ROW<id TINYINT, data STRING>')
def func2(data) -> Row:
    return Row(data.id, data.data*2)

table.map(func2).execute().print()

@udf(result_type = 'ROW<id BIGINT, data STRING>', func_type = 'pandas')
def func3(data):
    df = pd.concat([data.id, data.data], axis = 1)
    return df

table.map(func3).execute().print()