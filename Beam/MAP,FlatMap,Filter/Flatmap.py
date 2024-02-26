# MAP은 단일 입력에 대해 1개의 요소만 출력할 수 있지만, FlatMap은 단일 요소에 대해 여러 요소를 내보낼 수 있습니다.
import apache_beam as beam
p = beam.Pipeline()

line = (p
        | beam.io.ReadFromText('dept_data.txt')
        | beam.FlatMap(lambda record : record.split(','))
        # | beam.FlatMap(lambda record : record.split(',))
        | beam.Map(print)
        )

p.run()