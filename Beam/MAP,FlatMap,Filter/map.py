import apache_beam as beam

p = beam.Pipeline()

line = (p
        | "Read From file" >> beam.io.ReadFromText("dept_data.txt")
        | beam.Map(lambda record : record.split(','))
        | beam.Map(print)
        )

p.run()