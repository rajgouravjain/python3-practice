import sys
import re

from pyspark import SparkContext
from pyspark.sql.context import SQLContext
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.streaming import StreamingContext
from pyspark.mllib.clustering import KMeans, KMeansModel, StreamingKMeans
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.functions import udf
import operator



#########Spark conteext using spark session
#spark = SparkSession.builder \
#    .appName("streamingwithsql") \
#    .getOrCreate()
#sc = spark.sparkContext
###########
def streaming_to_df(rdd):
	 return sc.parallelize([Row(date='2018-09-20',latency=100)]).toDF()
	

sc = SparkContext(appName="streamingwithsql")
ssc = StreamingContext(sc, 5)
sqlContext = SQLContext(sc)
spark = sqlContext.sparkSession

indata_ds  = ssc.socketTextStream("localhost", 9999)
line_ds = indata_ds.map(lambda line: line.split(" "))
line_ds.pprint()


##Convert RDD string to RDD row
log_ds = line_ds.map(lambda w: Row(date='2018-09-20', latency=100) )
print("Hello DS",log_ds)

streaming_df = log_ds.foreachRDD(streaming_to_df)
print(streaming_df)
#schema_log = spark.createDataFrame(streaming_df)
#streaming_df.createOrReplaceTempView("log_ds")
  
#high_latency_df = spark.sql("Select date, latency from log_ds where latency > 100") 

#high_latency_df.pprint()
#high_latency_df.show()
#hl = high_latency_df.rrd.map(lambda l: "Latency: " + l.latency).collect()
ssc.start()
ssc.awaitTermination()
