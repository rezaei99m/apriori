from infrastructure.data_source.data_provider import DataProvider
from infrastructure.models.apriori import Apriori
# from infrastructure.models.set_model import SetModel

if __name__ == '__main__':
    fileName = input("First put your .csv data under ./infrastructure/data_source/datasets path and then enter csv data name e.g. 'data.csv':    ")
    minSupport = input("Enter your min support (it must be an integer number otherwise it throw an error):   ")
    data = DataProvider().readData(fileName=fileName)
    apriori = Apriori(data, minSupport=int(minSupport))
    apriori.run()
