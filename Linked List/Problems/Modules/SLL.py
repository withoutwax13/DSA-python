from typing import Counter


class Node(object):
    def __init__(self):
        self.data = None
        self.next = None

    def setData(self, data):
        if data != None:
            self.data = data
        else:
            self.data = None

    def setNext(self, nextNode):
        if nextNode != None:
            self.next = nextNode
        else:
            self.next = None

    def hasNext(self) -> bool:
        if self.next == None:
            return False
        else:
            return True

    def hasData(self) -> bool:
        if self.data == None:
            return False
        else:
            return True

    def getData(self) -> int:
        return self.data

    def getNext(self):
        return self.next


class SLL(object):
    def __init__(self):
        self.head = None

    def __iter__(self):
        self.x = 0
        return self

    def __next__(self):
        x = self.x
        if x >= self.length():
            raise StopIteration
        self.x = x + 1
        return self.getPosData(x)

    def create_node(self, data, next=None) -> Node:
        node = Node()
        node.setData(data)
        node.setNext(next)
        return node

    # Default insertion (end of the list)
    def insert(self, newData):
        if self.head == None:
            newNode = self.create_node(newData)
            self.head = newNode
        else:
            target = self.head
            while target.getNext() != None:
                target = target.getNext()
            newNode = self.create_node(newData)
            target.setNext(newNode)

    # Insertion at start
    def insertAtBegin(self, newData):
        newNode = self.create_node(newData, self.head)
        self.head = newNode

    # Insertion at desired pos at mid
    def insertAt(self, newData, pos):  # in pos, start ref is 0
        # check if pos is valid
        if self.length() > pos and pos > 0:
            prev = None
            target = self.head
            counter = 0
            while counter != pos:
                counter += 1
                prev = target
                target = target.getNext()
            newNode = self.create_node(newData, target)
            prev.setNext(newNode)
        else:
            raise ValueError("POS variable out of range")

    # Default deletion(end of the list)
    def delete(self):
        if self.head != None:
            prev = None
            target = self.head
            while target.getNext() != None:
                prev = target
                target = target.getNext()
            prev.setNext(None)

    # Deletion at start
    def deleteAtBegin(self):
        if self.head != None:
            next = self.head.getNext()
            self.head.setData(next.getData())
            self.head.setNext(next.getNext())

    # Deletion at intermediate Node
    def deleteAtMid(self, node):
        if self.head != None:
            prev = None
            target = self.head
            while target != node:
                prev = target
                target = target.getNext()
            link = target.getNext()
            prev.setNext(link)

    def deleteAt(self, pos):
        counter = 0
        target = self.head
        prev = None
        while target.getNext() != None:
            if counter == pos:
                break
            prev = target
            target = target.getNext()
        if prev == None:
            self.head = target.getNext()
        else:
            prev.setNext(target.getNext())

    # Delete SLL
    def clear(self):
        self.head = None

    # Return number of nodes
    def length(self) -> int:
        if self.head == None:
            return 0
        else:
            counter = 1
            target = self.head
            while target.getNext() != None:
                target = target.getNext()
                counter += 1
            return counter

    # Traverse all nodes and print data values
    def printList(self) -> None:
        result = " "
        target = self.head
        while target != None:
            result += f"{target.getData()} "
            target = target.getNext()
        print(result)

    def getPosData(self, pos):
        counter = 0
        target = self.head
        while counter < pos and target.getNext() != None:
            target = target.getNext()
            counter += 1
        return target.getData()

    def getHeadNode(self) -> Node:
        return self.head

    def getHeadData(self):
        return self.getPosData(0)

    def getTailData(self):
        return self.getPosData(self.length()-1)


# test Code for this module
if __name__ == "__main__":
    test_SLL = SLL()
    test_SLL.insert(1)
    test_SLL.insert(2)
    test_SLL.insertAtBegin(3)
    test_SLL.insertAt(4, 1)
    test_SLL.printList()
    print(test_SLL.getTailData())
