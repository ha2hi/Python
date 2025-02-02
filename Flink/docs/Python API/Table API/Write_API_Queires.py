from pyflink.table import EnvironmentSettings, TableEnvironment, DataTypes
from pyflink.table.expressions import call, col
from pyflink.table.udf import udf
import pandas as pd

env_settings = EnvironmentSettings.in_batch_mode()
t_env = TableEnvironment.create(env_settings)

orders = t_env.from_elements([('Jack', 'FRANCE', 10), ('Rose', 'ENGLAND', 30), ('Jack', 'FRANCE', 20)],
                                 ['name', 'country', 'revenue'])

# orders.execute().print()

# compute revenue for all customers from France
revenue = orders \
    .select(col("name"), col("country"), col("revenue")) \
    .where(col("country") == 'FRANCE') \
    .group_by(col("name")) \
    .select(col("name"), call("sum", col("revenue")).alias('rev_sum'))

revenue.execute().print()

map_function = udf(lambda x : pd.concat([x.name, x.revenue*10], axis = 1),
                   result_type = DataTypes.ROW(
                                [DataTypes.FIELD("name", DataTypes.STRING()),
                                DataTypes.FIELD("revenue", DataTypes.BIGINT())]),
                   func_type="pandas")

orders.map(map_function).execute().print()