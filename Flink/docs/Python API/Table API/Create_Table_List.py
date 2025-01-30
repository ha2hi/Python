from pyflink.table import EnvironmentSettings, TableEnvironment, DataTypes

env = EnvironmentSettings.in_batch_mode()
t_env = TableEnvironment.create(env)

table = t_env.from_elements([(1,'Hi'), (2, 'Hello')], ['id', 'data'])

# 테이블 출력
table.execute().print()

# 자동 스키마 확인
print('By default the type of the "id" column is %s.' % table.get_schema().get_field_data_type('id'))

table = t_env.from_elements([(1, 'Hi'), (2, 'Hello')],
                                DataTypes.ROW([DataTypes.FIELD("id", DataTypes.TINYINT()),
                                               DataTypes.FIELD("data", DataTypes.STRING())]))

# 수동 스키마 확인
print('Now the type of the "id" column is %s.' % table.get_schema().get_field_data_type('id'))
