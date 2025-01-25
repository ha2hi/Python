from pyflink.common import Time, Types
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.functions import KeyedProcessFunction, RuntimeContext
from pyflink.datastream.state import ValueStateDescriptor 

env = StreamExecutionEnvironment.get_execution_environment()

class Sum(KeyedProcessFunction):
    def __init__(self):
        self.state = None
    
    def open(self, runtime_context: RuntimeContext):
        state_descriptor = ValueStateDescriptor("state", Types.FLOAT())
        self.state = runtime_context.get_state(state_descriptor)

    def process_element(self, value, ctx):
        current = self.state.value()

        if current is None:
            current = 0
        
        current += value[1]
        self.state.update(current)

        yield value[0], current


ds = env.from_collection(
  collection = [
    ('Alice', 110.1),
    ('Bob', 30.2),
    ('Alice', 20.1),
    ('Bob', 53.1),
    ('Alice', 13.1),
    ('Bob', 3.1),
    ('Bob', 16.1),
    ('Alice', 20.1)
  ],
  type_info = Types.TUPLE([Types.STRING(), Types.FLOAT()])
)

ds.key_by(lambda x : x[0]).process(Sum()).print()
env.execute()