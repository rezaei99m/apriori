from __future__ import annotations
from domain.entity.set_entity import SetEntity
import itertools


class SetModel(SetEntity):

    def __init__(self, items: list, setLength: int, supCount: int) -> None:
        self.items = items
        self.length = setLength
        self.supCount = supCount

    def join(self, setEntity: SetModel) -> SetModel:
        items = list(set(self.items + setEntity.items))
        return SetModel(items, len(items), 0)

    def subsets(self, n: int) -> list[SetModel]:
        allSubset = list(itertools.combinations(self.items, n))
        allSubsetSetModel = []
        for subset in allSubset:
            allSubsetSetModel.append(SetModel(list(subset), n, 0))
        return allSubsetSetModel

    def isSubset(self, setEntity: SetModel) -> bool:
        if set(setEntity.items).issubset(set(self.items)):
            return True
        else:
            return False

    def __str__(self):
        items_str = ''
        items_str += '{'
        for item in self.items:
            items_str += '{0}, '.format(str(item))
        items_str += '}'
        setToString = 'set: {0}, supCount: {1}, setLength: {2}'.format(items_str, self.supCount, self.length)

        return setToString

    def __eq__(self, other: SetModel):
        if len(self.items) != len(other.items):
            return False

        itemSet = set(self.items)
        itemSetOther = set(other.items)

        if itemSet == itemSetOther:
            return True
        else:
            return False
