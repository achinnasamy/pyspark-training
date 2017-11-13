from __future__ import print_function

from pyspark.conf import SparkConf
from pyspark.context import SparkContext
from pyspark.storagelevel import StorageLevel

config = SparkConf()
config.setMaster("local[*]")
config.setAppName("WORD_COUNT_JOB")


sc = SparkContext(conf=config)

textFileRDD = sc.textFile("/home/dharshekthvel/Desktop/ac/code/scalatrainingintellij/data/document.txt")


textFileRDD.persist(StorageLevel.MEMORY_AND_DISK)
textFileRDD.unpersist()



count_of_words = textFileRDD.flatMap(lambda each: each.split(' '))\
    .map(lambda each: (each,1))\
    .reduceByKey(lambda a,b:a+b).collect()



for (word,count) in count_of_words:
    print("%s - %s" % (word,count))