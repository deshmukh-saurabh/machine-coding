from models.store import Store
from services.store_service_interface import StoreServiceInterface


class StoreService(StoreServiceInterface):
    store_objects = {}

    def addStoreObject(self, store_object):
        self.__class__.store_objects.update(store_object)

    def deleteStoreObject(self, key):
        self.__class__.store_objects.pop(key)

    def getStoreKeys(self):
        return self.__class__.store_objects.keys()

    def searchStore(self, key, value):
        store_objects = self.__class__.store_objects
        respKeys = []
        for k, v in store_objects.items():
            if key in v and v[key] == value:
                respKeys.append(k)
        if not respKeys:
            return f"Could not find key: {key}, value: {value}"
        return ", ".join(respKeys)

    def getValue(self, key):
        store_keys = self.getStoreKeys()
        if key not in store_keys:
            return f"No entry found for {key}"
        return self.__class__.store_objects.get(key)
