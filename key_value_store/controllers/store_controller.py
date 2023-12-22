class StoreController(object):
    def __init__(self, storeService):
        self.storeService = storeService

    def addStoreObject(self, store_object):
        self.storeService.addStoreObject(store_object)

    def deleteStoreObject(self, key):
        self.storeService.deleteStoreObject(key)

    def getStoreKeys(self):
        storeKeys = list(self.storeService.getStoreKeys())
        return ", ".join(storeKeys)

    def searchStore(self, key, value):
        return self.storeService.searchStore(key, value)

    def getValue(self, key):
        return self.storeService.getValue(key)
