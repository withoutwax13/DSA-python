class Node(object):
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

    def setLeft(self, node):
        self.left = node

    def setRight(self, node):
        self.right = node

    def setData(self, data):
        self.data = data

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getData(self):
        return self.data

    def hasLeft(self) -> bool:
        return self.left != None

    def hasRight(self) -> bool:
        return self.right != None
