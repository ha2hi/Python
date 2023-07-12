import apache_beam as beam

p = beam.Pipeline()

line = (p
        | beam.Create({'row1' : [1,2,3,4,5],
                       'row2' : [1,2,3,4,5]})
        | beam.Map(print)
        )
p.run()