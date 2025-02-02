from pyflink.table.expressions import col
from pyflink.table import EnvironmentSettings, TableEnvironment
import pandas as pd
import numpy as np

env_settings = EnvironmentSettings.in_batch_mode()
t_env = TableEnvironment.create(env_settings)

pdf = pd.DataFrame(np.random.rand(1000, 2))
table = t_env.from_pandas(pdf, ["a", "b"]).filter(col('a') > 0.5)

print(table.limit(5).to_pandas())