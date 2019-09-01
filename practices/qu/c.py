from pyspark import SparkContext
from pyspark.streaming import StreamingContext

# Create a local StreamingContext with two working thread and batch interval of 15 second
sc = SparkContext("local[2]", "NetworkWordCount")
ssc = StreamingContext(sc, 5)

lines = ssc.socketTextStream("localhost", 9999)

words_ds = lines.map(lambda line: line.split(" "))

success_message_ds = words_ds.filter(lambda words: " ".join((words[-3],words[-2],words[-1])) == "Everything looks good" )
error_message_ds = words_ds.filter(lambda words: " ".join((words[-3],words[-2],words[-1])) != "Everything looks good" )

success_message_ds.pprint()
error_message_ds.pprint()

#ds = words_ds.filter(lambda words: int(words[4].rstrip('ms]').lstrip('[')) > 100 )

# Print the first ten elements of each RDD generated in this DStream to the console
#words_ds1.pprint()
ssc.start()             # Start the computation
ssc.awaitTermination()  # Wait for the computation to terminate
