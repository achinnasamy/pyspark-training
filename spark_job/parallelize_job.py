from __future__ import print_function
from pyspark.conf import SparkConf
from pyspark.context import SparkContext



config = SparkConf()
config.setMaster("local[*]")
config.setAppName("ParallelizeJOB")


sc = SparkContext(conf=config)
dataRDD = sc.parallelize([100,200,300,400])


#<class 'pyspark.rdd.RDD'>
print(type(dataRDD))

dataRDD.foreach(lambda eachElement: print(eachElement))
