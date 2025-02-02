from pyflink.table import EnvironmentSettings, TableEnvironment, DataTypes
import pandas as pd
import numpy as np

env_settings = EnvironmentSettings.in_batch_mode()
t_env = TableEnvironment.create(env_settings)

pdf = pd.DataFrame(np.random.rand(1000,2))
table = t_env.from_pandas(pdf,
                          DataTypes.ROW([DataTypes.FIELD("f0", DataTypes.DOUBLE()),
                                         DataTypes.FIELD("f1", DataTypes.DOUBLE())]))

table.limit(5).execute().print()