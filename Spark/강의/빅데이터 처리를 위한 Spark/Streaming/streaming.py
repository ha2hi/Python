# 소켓 열기 : nc -lk 9999
# 입력 1 : spark sql streaming
# 입력 2 : spark graphx pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.appName("streaming-word-count").getOrCreate()

lines_df = spark.readStream.format("socket")\
                           .option("host", "localhost")\
                           .option("port", "9999")\
                           .load()

words_df = lines_df.select(expr("explode(split(value, ' ')) as word"))
counts_df = words_df.groupBy("word").count()
ㅕ7777777777777777
word_count_query = counts_df.writeStream.format("console")\
                                        .outputMode("complete")\
                                        .option("checkpointLocation", ".checkpoint")\
                                        .start()

word_count_query.awaitTermination()