# DataStream 환경을 기반으로 Table 인스턴스를 생성 후 DataStream 환경을 수정하면 생성한 Table 인스턴스에 반영이 안됩니다.
# 따라서 Table 인스턴스를 생성하기전에 DataStream 환경 설정을 모두 작업하고 인스턴스를 생성해야 됩니다.
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import StreamTableEnvironment
from pyflink.datastream.checkpointing_mode import CheckpointingMode

from pyflink.java_gateway import get_gateway

env = StreamExecutionEnvironment.get_execution_environment()

env.set_max_parallelism(256)
env.get_checkpoint_config().set_checkpointing_mode(CheckpointingMode.EXACTLY_ONCE)

t_env = StreamTableEnvironment.create(env)
t_env.get_config().set_local_timezone("Asia/Seoul")