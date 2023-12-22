class User(object):
    def __init__(self):
        self.id = None
        self.name = None

    def setUserId(self, id):
        self.id = id

    def getUserId(self):
        return self.id

    def setUserName(self, name):
        self.name = name

    def getUserName(self, name):
        return self.name
