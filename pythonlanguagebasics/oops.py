

class AbstractInvestment:

    def loadData(self, data):
        print(data)



class Investment:

    def loadInvestments(self, data):
        print data



class InvestmentConclave:


    def __init__(self, _timeline_):
        self.timeline = _timeline_


    def computeSparkIngestion(self, run):
        print(run)

    @staticmethod
    def save_in_hdfs(hdfs_data):
        print(hdfs_data)



# Extending two classes

class PrivateBanking(AbstractInvestment, Investment):
    pass



in_conclave = InvestmentConclave("TimeLine")

in_conclave.computeSparkIngestion("RUN SPARK")


InvestmentConclave.save_in_hdfs("HDFS DATA")



pb = PrivateBanking()

pb.loadData("DATA FROM PRIVATEBANKING")
pb.loadInvestments("DATA FOR INVESTMENTS")