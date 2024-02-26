from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaseter('local').setAppName('count-reviews')
sc = SparkContext(conf = conf)

lines = sc.textFile("file:///data/restaurant_reviews.csv")

header = lines.first()
filter_lines = lines.filter(lambda row: row != header)

def parse(filter_lines):
    data = filter_lines.split(',')
    return (str(data[2]), int(data[3]))

categoryReviews = filter_lines.map(parse)

categoryReviewsCount = categoryReviews.mapValues(lambda x : (x,1))

reduced = categoryReviewsCount.reduceByKey(lambda x, y : (x[0] + y[0], x[1]+y[1]))

averages = reduced.mapValues(lambda x : x[0] / x[1])

averages.collect()