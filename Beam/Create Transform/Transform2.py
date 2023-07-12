import apache_beam as beam

p = beam.Pipeline()

line = (p
        | beam.Create([("maths", 52), ("english", 75), ("science", 82)])
        | beam.Map(print)
        )

p.run()