from pyflink.table import EnvironmentSettings, TableEnvironment
from pyflink.table import DataTypes

t_env = TableEnvironment.create(EnvironmentSettings.in_streaming_mode())


table = t_env.from_elements([(1, 'Hi'), (2, 'Hello')],
                                DataTypes.ROW([DataTypes.FIELD("id", DataTypes.TINYINT()),
                                               DataTypes.FIELD("data", DataTypes.STRING())]))

print(table.get_schema())