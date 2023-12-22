class Group(object):
    def __init__(self):
        self.id = None
        self.name = None
        self.members = None

    def setGroupId(self, id):
        self.id = id

    def getGroupId(self):
        return self.id

    def setGroupName(self, name):
        self.name = name

    def getGroupName(self):
        return self.name

    def setGroupMembers(self, members):
        self.members = members

    def getGroupMembers(self):
        return self.members
