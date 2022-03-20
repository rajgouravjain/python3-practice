from pyspark import SparkContext
from pyspark.streaming import StreamingContext

# Create a local StreamingContext with two working thread and batch interval of 1 second
sc = SparkContext("spark://3eebf8abdddc:7077", "LogWordCount")
ssc = StreamingContext(sc, 5)


lines = ssc.socketTextStream("192.168.43.214", 9999)

words = lines.flatMap(lambda line: line.split(","))

pairs = words.map(lambda word: (word, 1))

wordCounts = pairs.reduceByKey(lambda x, y: x + y)


windowCounts = wordCounts.window(15,10).count()
windowCounts.pprint()

ssc.start()             # Start the computation
ssc.awaitTermination() 
