from __future__ import print_function
from pyspark import SparkConf
from pyspark import SparkContext


sparkconfig = SparkConf()
sparkconfig.setMaster("local[*]")
sparkconfig.setAppName("SparkCSVJOB")

def compute_each_line(eachLine):

    # Fetching the broadcast
    date_code = date_code_broadcast.value

    data_split = eachLine.split(",")

    if data_split[0] in date_code:
        print(eachLine)

    return



sparkcontext = SparkContext(conf= sparkconfig)

date_code_broadcast = sparkcontext.broadcast(["20170104", "20170102"])

textFileRDD = sparkcontext.textFile("/home/dharshekthvel/Downloads/query_result.csv")

textFileRDD.map(compute_each_line).collect()


