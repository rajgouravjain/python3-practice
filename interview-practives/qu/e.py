import sys
import re

from pyspark import SparkContext
from pyspark.sql.context import SQLContext
from pyspark.sql import SparkSession

from pyspark.mllib.clustering import KMeans, KMeansModel, StreamingKMeans

from pyspark.sql.functions import *
from pyspark.sql.types import *


import operator



######Spark Session using spark context
#sc = SparkContext(appName="streamingwithsql")
#ssc = StreamingContext(sc, 5)
#sqlContext = SQLContext(sc)
#spark = sqlContext.sparkSession

#########Spark context using spark session
spark = SparkSession \
    .builder \
    .appName("1streamingwithsql") \
    .getOrCreate()
sc = spark.sparkContext
#ssc = StreamingContext(sc, 5)
sqlContext = SQLContext(sc)

spark.conf.set("spark.sql.streaming.checkpointLocation", "./l")
###########

lines = spark \
    .readStream \
    .format("socket") \
    .option("host", "localhost") \
    .option("port", 9999) \
    .load()
print("DF lines is:",lines)
print(lines.isStreaming)
print(lines.printSchema())

words = lines.select(
   explode(
       split(lines.value, " ")
   ).alias("word")
)
print("DF words is:",words)
# Generate running word count
wordCounts = words.groupBy("word").count()

query = wordCounts \
    .writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()

#indata_ds.show()
#line_ds = indata_ds.map(lambda line: line.split(" "))
#line_ds.pprint()
