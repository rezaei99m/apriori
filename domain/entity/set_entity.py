from __future__ import annotations
from abc import ABC, abstractmethod


class SetEntity(ABC):

    @abstractmethod
    def join(self, setEntity) -> SetEntity:
        """
        :param setEntity: join the set with setEntity
        :return: SetEntity
        """
        pass

    @abstractmethod
    def isSubset(self, setEntity) -> bool:
        """
        :param setEntity: set we want to check if it is a subset of the set
        :return: if setEntity is subset of the set
        """
        pass

    @abstractmethod
    def subsets(self, n: int) -> list[SetEntity]:
        """
        return
        :param n: number of members for subsets
        :return: list of all n-item subsets
        """
        pass
