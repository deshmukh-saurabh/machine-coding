class Store(object):
    def __init__(self):
        self.store_objects = {}

    def getStoreObjects(self):
        return self.store_objects

    def setStoreObjects(self, store_objects):
        self.store_objects = store_objects
