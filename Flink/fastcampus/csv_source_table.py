from pyflink.table import EnvironmentSettings, TableEnvironment, DataTypes, CsvTableSource

table_env = TableEnvironment.create(EnvironmentSettings.in_batch_mode())

field_name = ["framework", "chapter"]
field_type = [DataTypes.STRING(), DataTypes.BIGINT()]

source = CsvTableSource(
    "./data/sample.csv",
    field_name,
    field_type,
    ignore_first_line=False
)

table_env.register_table_source("chapters", source)
table = table_env.from_path("chapters")

print(table.to_pandas())