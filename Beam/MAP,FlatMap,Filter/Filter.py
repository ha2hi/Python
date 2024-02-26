import apache_beam as beam

def SplitRow(element):
    return element.split(',')

def filtering(record):
    return record[3] == "Accounts"

with beam.Pipeline() as p:
    (p
     | "Read From File" >> beam.io.ReadFromText("dept_data.txt")
     | beam.Map(SplitRow)
     | beam.Filter(filtering)
     | beam.Map(print)     
    )