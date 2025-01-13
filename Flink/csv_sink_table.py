from pyflink.table import (
    EnvironmentSettings, TableEnvironment, DataTypes, CsvTableSource,
    CsvTableSink, WriteMode
)

t_env = TableEnvironment.create(EnvironmentSettings.in_batch_mode())

src_field_name = ["framework", "chapter"]
src_field_type = [DataTypes.STRING(), DataTypes.BIGINT()]

source = CsvTableSource(
    "./data/sample.csv",
    src_field_name,
    src_field_type,
    ignore_first_line=False
)

t_env.register_table_source("chapters", source)
table = t_env.from_path("chapters")

table.print_schema()


out_field_names = ["framework", "chapter"]
out_field_types = [DataTypes.STRING(), DataTypes.BIGINT()]
sink = CsvTableSink(
  out_field_names,
  out_field_types,
  './sample_copy.csv',
  num_files=1,
  write_mode=WriteMode.OVERWRITE
)
t_env.register_table_sink('out', sink)

table.execute_insert('out').wait()
# t_env.execute("sample_copy")