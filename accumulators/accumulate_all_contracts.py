from __future__ import print_function
from pyspark import SparkConf
from pyspark import SparkContext


sparkconfig = SparkConf()
sparkconfig.setMaster("local[*]")
sparkconfig.setAppName("SparkCSVJOB")

def print_each_line(eachLine):
    print (eachLine)
    return


sparkcontext = SparkContext(conf= sparkconfig)

date_accumulator = sparkcontext.accumulator(0)

textFileRDD = sparkcontext.textFile("/home/dharshekthvel/Downloads/query_result.csv")

textFileRDD.map(lambda each : each.split(","))\
    .map(lambda each: date_accumulator.add(1) if each[0]=="20170103" else date_accumulator.add(0))\
    .collect()


print (date_accumulator.value)
    #.foreach(lambda each : print(each[0]))

#textFileRDD.foreach(print_each_line)


