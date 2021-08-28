import queue
from Node import Node
from queue import Queue


class BT(object):

    """
        Basic Operations:
            1. Inserting an element into a tree
            2. Deleting an element into a tree
            3. Searching for an element
            4. Traversing the tree

        Aux operations:
            1. Finding the size of the tree
            2. Finding the height of the tree
            3. Finding the level which has the maximum sum
            4. Finding the least common ancestor for a given pair of nodes and many more
    """

    def __init__(self) -> None:
        self.head = None

    def create_node(self, data) -> Node:
        node = Node()
        node.setData(data)
        return node

    ### START OF TRAVERSAL OPERATIONS ###

    # PREORDER TRAVERSAL
    def preTraversal(self, current=None, printM=[]):
        if current == None:
            current = self.head
        printM.append(current.getData())
        if current.hasLeft():
            self.preTraversal(current.getLeft(), printM)
        if current.hasRight():
            self.preTraversal(current.getRight(), printM)
        else:
            return

    # INORDER TRAVERSAL
    def inTraversal(self, current=None, printM=[]):
        if current == None:
            current = self.head
        if current.hasLeft():
            self.inTraversal(current.getLeft(), printM)
        if current.hasRight():
            printM.append(current.getData())
            self.inTraversal(current.getRight(), printM)
        else:
            printM.append(current.getData())
            return

    # POSTORDER TRAVERSAL
    def postTraversal(self, current=None, printM=[]):
        if current == None:
            current = self.head
        if current.hasLeft():
            self.postTraversal(current.getLeft(), printM)
        if current.hasRight():
            self.postTraversal(current.getRight(), printM)
        printM.append(current.getData())
        return

    # LEVEL ORDER TRAVERSAL
    def levelTraversal(self, printM):
        if self.head == None:
            return
        q = Queue()
        q.put(self.head)
        current = None

        while not q.empty():
            current = q.get()
            printM.append(current.getData())
            if current.hasLeft():
                q.put(current.getLeft())
            if current.hasRight():
                q.put(current.getRight())
    ### END OF TRAVERSAL OPERATIONS ###

    # returns true if a data param is present in a tree element

    def isElementPresent(self, data, current=None) -> bool:
        if current == None:
            current = self.head
        if current.getData() != data:
            if current.hasLeft() or current.hasRight():
                return self.isElementPresent(data, current.getLeft()) or self.isElementPresent(data, current.getRight())
            else:
                return False
        else:
            return True

    # insert data on node's left
    def insertLeft(self, data, node):
        leftNode = self.create_node(data)
        if node.hasLeft() == None:
            node.setLeft(leftNode)
        else:
            tempNode = node.getLeft()
            leftNode.setLeft(tempNode)
            node.setLeft(leftNode)

    # insert data on node's right
    def insertRight(self, data, node):
        rightNode = self.create_node(data)
        if node.hasRight() == None:
            node.setRight(rightNode)
        else:
            tempNode = node.getRight()
            rightNode.setRight(tempNode)
            node.setRight(rightNode)

    # insert data on the tree
    def insert(self, data):
        q = Queue()
        q.put(self.head)
        current = None
        while not q.empty():
            current = q.get()
            if current == None:
                self.head = self.create_node(data)
                break
            else:
                if current.hasLeft():
                    q.put(current.getLeft())
                else:
                    newNode = self.create_node(data)
                    current.setLeft(newNode)
                    break
                if current.hasRight():
                    q.put(current.getRight())
                else:
                    newNode = self.create_node(data)
                    current.setRight(newNode)
                    break

    # delete tree
    def deleteTree(self):
        self.head = None

    # find size
    def size(self, current=None):
        q = Queue()
        if self.head == None:
            return 0
        q.put(current or self.head)
        current = None
        size = 0
        while not q.empty():
            current = q.get()
            if current.hasLeft():
                q.put(current.getLeft())
            if current.hasRight():
                q.put(current.getRight())
            size = size + 1
        return size

    # print tree elements in reverse order
    def printReverse(self, current=None):
        q = Queue()
        if self.head == None:
            return
        q.put()


class Strict_BT(BT):
    def __init__(self) -> None:
        super().__init__()


class Full_BT(BT):
    def __init__(self) -> None:
        super().__init__()


class Complete_BT(BT):
    def __init__(self) -> None:
        super().__init__()


if __name__ == "__main__":
    bt = BT()
    bt.insert(1)
    bt.insert(2)
    bt.insert(3)
    bt.insert(4)
    bt.insert(5)
    printM = []
    bt.levelTraversal(printM)
    print(printM)
    print(bt.size())
