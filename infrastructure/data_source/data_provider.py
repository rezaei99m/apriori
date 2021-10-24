import pandas as pd
from csv import reader


class DataProvider:
    def __init__(self) -> None:
        pass

    @staticmethod
    def readData(fileName: str) -> list[list[str]]:

        data = []
        with open('infrastructure/data_source/datasets/{0}'.format(fileName), 'r') as csv_data:
            _data = reader(csv_data)
            for line in _data:
                if '' in line:
                    line.remove('')
                data.append(line)
        
        
        return data
