class Node(object):
    def __init__(self):
        self.prev = None
        self.next = None
        self.data = None

    def setPrev(self, node):
        self.prev = node

    def setNext(self, node):
        self.next = node

    def setData(self, data):
        self.data = data

    def getPrev(self):
        return self.prev

    def getNext(self):
        return self.next

    def getData(self):
        return self.data

    def hasNext(self) -> bool:
        return self.next != None

    def hasPrev(self) -> bool:
        return self.prev != None


class DLL(object):

    def __init__(self):
        self.head = None

    def create_node(self, data, prev=None, next=None) -> Node:
        node = Node()
        node.setData(data)
        node.setPrev(prev)
        node.setNext(next)
        return node

    # Default insertion (next of head)
    def insert(self, data):
        if self.head == None:
            newNode = self.create_node(data)
            self.head = newNode
        else:
            if self.head.hasNext():
                nextOfHead = self.head.getNext()
                newNode = self.create_node(data, self.head, nextOfHead)
                self.head.setNext(newNode)
                nextOfHead.setPrev(newNode)
            else:
                newNode = self.create_node(data, self.head)
                self.head.setNext(newNode)

    def insertAsTail(self, data):
        if self.head == None:
            newNode = self.create_node(data)
            self.head = newNode
        else:
            target = self.head
            while target.getNext() != None:
                target = target.getNext()
            newNode = self.create_node(data, target)
            target.setNext(newNode)

    def insertAt(self, pos, data):
        if self.head == None:
            newNode = self.create_node(data)
            self.head = newNode
        else:
            if pos < (self.length() - 1) and pos > 0:
                target = self.head
                targetprev = None
                counter = 0
                while counter != pos:
                    targetprev = target
                    target = target.getNext()
                    counter += 1
                newNode = self.create_node(data, targetprev, target)
                target.setPrev(newNode)
                targetprev.setNext(newNode)
            else:
                raise ValueError("pos out of range")

    # Default deletion (tail node)
    def delete(self):
        target = self.head
        while target.getNext() != None:
            target = target.getNext()
        newTail = target.getPrev()
        newTail.setNext(None)

    def deleteHead(self):
        newHead = self.head.getNext()
        newHead.setPrev(None)
        self.head = newHead

    def deleteAt(self, pos):
        if pos < (self.length() - 1) and pos > 0:
            counter = 0
            target = self.head
            while counter != pos:
                target = target.getNext()
                counter += 1
            prevTarget = target.getPrev()
            nextTarget = target.getNext()
            prevTarget.setNext(nextTarget)
            nextTarget.setPrev(prevTarget)
        else:
            raise ValueError("pos out of range")

    def length(self) -> int:
        target = self.head
        counter = 1
        while target.hasNext():
            counter += 1
            target = target.getNext()
        return counter

    def print(self):
        result = ""
        target = self.head
        while target != None:
            result += f" {target.getData()}"
            target = target.getNext()
        print(result)

    def clear(self):
        self.head = None


# test Code for this module
if __name__ == "__main__":
    test_DLL = DLL()
    test_DLL.insert(1)
    test_DLL.insert(2)
    test_DLL.insertAsTail(4)
    test_DLL.insertAt(1, 3)
    print(test_DLL.length())
    test_DLL.print()
