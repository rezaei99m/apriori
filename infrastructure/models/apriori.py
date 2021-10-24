from infrastructure.models.set_model import SetModel
import collections


class Apriori:
    def __init__(self, data: list[list[str]], minSupport: int) -> None:
        self.__data = data
        self.__minSupport = minSupport

    def run(self, ) -> None:
        frequentSetsList = []  # this is list of all k-item frequent subset
        L1FrequentSets = self.__findL1FrequentSets()
        frequentSetsList.append(L1FrequentSets)
        k = 2  # in here we use k = 2 since our 1-item frequent set extracted
        while True:
            if len(frequentSetsList[k-2]) == 0:
                break
            Ck = self.__aprioriGenerator(frequentSetsList[k-2])
            for i in range(0, len(Ck)):
                for transaction in self.__data:
                    if set(Ck[i].items).issubset(set(transaction)):
                        Ck[i].supCount += 1
            lk = [x for x in Ck if x.supCount >= self.__minSupport]
            frequentSetsList.append(lk)
            k += 1

        # print all frequent set
        counter = 1
        for _list in frequentSetsList:
            print('{0}-item set'.format(counter))
            for _set in _list:
                print(_set)
            print('==============')
            counter += 1

    def __aprioriGenerator(self, frequentSets: list[SetModel]) -> list[SetModel]:
        """
        :param frequentSets: list of all frequent set with length k-1
        :return: list of all possible frequent subsets
        """
        Ck = []
        for l1 in frequentSets:
            for l2 in frequentSets:
                if self.__canJoinTogether(l1, l2):
                    newSet = l1.join(l2)
                    if not self.__hasInfrequentSubsets(newSet, frequentSets):
                        if newSet not in Ck:  # add set if it is not in the Ck
                            Ck.append(newSet)
        return Ck

    @staticmethod
    def __canJoinTogether(set1: SetModel, set2: SetModel) -> bool:
        if len(set1.items) != len(set2.items):
            return False
        else:
            if len(set(set1.items).symmetric_difference(set(set2.items))) != 2:
                return False
            else:
                return True

    @staticmethod
    def __hasInfrequentSubsets(sourceSet: SetModel, previousFrequentSubsets: list[SetModel],) -> bool:
        """
        :param sourceSet: the set we want to check whether it hase any infrequent subset
        :param previousFrequentSubsets: lit of all frequent (k-1)-item set
        :return: return true if it has any infrequent subset and false otherwise
        """
        subsetLength = len(previousFrequentSubsets[0].items)
        allSubsets = sourceSet.subsets(subsetLength)
        hasInfrequentSubset = False
        for subset in allSubsets:
            isSubsetInfrequent = True
            for frequentSet in previousFrequentSubsets:
                if collections.Counter(subset.items) == collections.Counter(frequentSet.items):
                    isSubsetInfrequent = False
            hasInfrequentSubset = isSubsetInfrequent or hasInfrequentSubset
        return hasInfrequentSubset

    def __findL1FrequentSets(self) -> list[SetModel]:
        L1_frequent_sets = []
        all_transaction_items = []
        for transaction in self.__data:
            for item in transaction:
                if item not in all_transaction_items:
                    all_transaction_items.append(item)

        for transactionItem in all_transaction_items:
            counter = 0
            for transaction in self.__data:
                if transactionItem in transaction:
                    counter += 1
            if counter >= self.__minSupport:
                setModel = SetModel([transactionItem], 1, counter)
                L1_frequent_sets.append(setModel)
        return L1_frequent_sets
