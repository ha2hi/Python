import apache_beam as beam

def SplitRow(element):
    return element.split(',')

with beam.Pipeline() as p:
    input_collection = (
        p 
         | "Read From Text File" >> beam.io.ReadFromText("dept_data.txt")
         | beam.Map(SplitRow)
    )

    accounts_count = (
                      input_collection
                      | 'Get all Accounts dept persons' >> beam.Filter(lambda record: record[3] == 'Accounts')
                      | 'Pair each accounts employee with 1' >> beam.Map(lambda record: ("Accounts, " +record[1], 1))
                      | 'Group and sum1' >> beam.CombinePerKey(sum)
                 )

    hr_count = (
                input_collection
                | 'Get all HR dept persons' >> beam.Filter(lambda record: record[3] == 'HR')
                | 'Pair each hr employee with 1' >> beam.Map(lambda record: ("HR, " +record[1], 1))
                | 'Group and sum' >> beam.CombinePerKey(sum)
           )
    
    output = (
         (accounts_count,hr_count)
                | beam.Flatten()
                | beam.Map(print)
            )