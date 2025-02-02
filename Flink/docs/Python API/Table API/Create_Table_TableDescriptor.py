from pyflink.table import EnvironmentSettings, TableEnvironment, TableDescriptor, Schema, DataTypes

env = EnvironmentSettings.in_streaming_mode()
t_env = TableEnvironment.create(env)

t_env.create_temporary_table(
    'random_source',
    TableDescriptor.for_connector('datagen')
        .schema(Schema.new_builder()
                .column('id', DataTypes.BIGINT())
                .column('data', DataTypes.TINYINT())
                .build())
        .option('fields.id.kind', 'sequence')
        .option('fields.id.start', '1')
        .option('fields.id.end', '3')
        .option('fields.data.kind', 'sequence')
        .option('fields.data.start', '4')
        .option('fields.data.end', '6')
        .build())

table = t_env.from_path('random_source')
table.execute().print()