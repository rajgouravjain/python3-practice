from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext
from pyspark.sql.types import StructType, StructField, TimestampType, StringType
from pyspark.sql.functions import window

# Create a local StreamingContext with two working thread and batch interval of 1 second
spark = SparkSession.builder.master("spark://3eebf8abdddc:7077") \
             .appName("LogWordCount") \
             .getOrCreate()

#             .config("spark.sql.warehouse.dir", dataDirectory) \
logSchema = StructType([
              StructField("timestamp", TimestampType(), True),
              StructField("message", StringType(), True)
])

##Socket example
logDF = spark \
    .readStream \
    .format("csv") \
    .option("sep", ",") \
    .schema(logSchema) \
    .csv("file:///var/log/csv/")

print("Is Streaming : ",logDF.isStreaming)
print("Print schema : ",logDF.printSchema())


windowedCounts = logDF.withWatermark("timestamp", "10 seconds").groupBy(
    window(logDF.timestamp, "30 seconds", "15 seconds"),
    "message"
).count()

query = windowedCounts \
    .writeStream \
    .format("console") \
    .outputMode("complete") \
    .start()

query.awaitTermination()
