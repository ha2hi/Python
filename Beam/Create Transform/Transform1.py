import apache_beam as beam

p = beam.Pipeline()

lines = (
    p | beam.Create(['a','b','c'])
      | beam.Map(print)
)

p.run()