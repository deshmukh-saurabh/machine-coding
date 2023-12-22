import abc


class StoreServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addStoreObject(self, store_object):
        pass

    @abc.abstractmethod
    def deleteStoreObject(self, key):
        pass

    @abc.abstractmethod
    def getStoreKeys(self):
        pass

    @abc.abstractmethod
    def searchStore(self, key, value):
        pass

    @abc.abstractmethod
    def getValue(self, key):
        pass
