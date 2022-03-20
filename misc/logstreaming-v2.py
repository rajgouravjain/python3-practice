from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext
from pyspark.sql.types import StructType, StructField, TimestampType, StringType
from pyspark.sql.functions import window

# Create a local StreamingContext with two working thread and batch interval of 1 second
spark = SparkSession.builder.master("spark://3eebf8abdddc:7077") \
             .appName("LogWordCount") \
             .config("spark.sql.warehouse.dir", dataDirectory) \
             .getOrCreate()

##Socket example
socketDF = spark \
    .readStream \
    .format("socket") \
    .option("host", "192.168.43.214") \
    .option("port", 9999) \
    .option("includeTimestamp", True) \
    .load()

print("Is Streaming : ",socketDF.isStreaming)
print("Print schema : ",socketDF.printSchema())


windowedCounts = socketDF.withWatermark("timestamp", "10 seconds").groupBy(
    window(socketDF.timestamp, "30 seconds", "15 seconds"),
    "value"
).count()

query = windowedCounts \
    .writeStream \
    .format("console") \
    .outputMode("complete") \
    .start()

query.awaitTermination()
