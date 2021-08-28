class Node(object):
    def __init__(self):
        self.data = None
        self.next = None

    def setData(self, data):
        self.data = data

    def setNext(self, next):
        self.next = next

    def getData(self) -> int:
        return self.data

    def getNext(self):
        return self.next


class CLL(object):
    """
        Class representation of a circlular linked list data structure

        All insertions are O(n) + O(1)

    """

    def __init__(self):
        self.head = None

    # O(1)
    def create_node(self, data, next=None) -> Node:
        node = Node()
        node.setData(data)
        node.setNext(next)
        return node

    # Default insertion(insert after head)
    def insert(self, data):
        if self.head == None:
            newNode = self.create_node(data)
            newNode.setNext(newNode)
            self.head = newNode
        else:
            headNext = self.head.getNext()
            newNode = self.create_node(data, headNext)
            self.head.setNext(newNode)

    # Insert at a pos after head
    def insertAt(self, pos, data):
        if pos < 1 or pos > (self.length()):
            raise ValueError("Pos out of range")
        counter = 0
        target = self.head
        prev = None
        while counter != pos:
            prev = target
            target = target.getNext()
            counter += 1
        newNode = self.create_node(data, target)
        prev.setNext(newNode)

    # Insert before head
    def insertPostHead(self, data):
        newNode = self.create_node(data, self.head)
        preHead = self.head
        while preHead.getNext() != self.head:
            preHead = preHead.getNext()
        preHead.setNext(newNode)

    # Default deletion (delete pre-head)
    def delete(self):
        preHead = self.head
        prev = None
        while preHead.getNext() != self.head:
            prev = preHead
            preHead = preHead.getNext()
        prev.setNext(self.head)

    # Delete head
    def deleteHead(self):
        newHead = self.head.getNext()
        self.head = newHead

    def length(self) -> int:
        if self.head == None:
            return 0
        counter = 0
        target = self.head.getNext()
        while target != self.head:
            counter += 1
            target = target.getNext()
        return counter + 1

    def print(self):
        if self.head == None:
            print("")
        else:
            result = f"{self.head.getData()} "
            target = self.head.getNext()
            while target != self.head:
                result += f"{target.getData()} "
                target = target.getNext()
            print(result)


if __name__ == "__main__":
    test_cll = CLL()
    test_cll.insert(1)
    test_cll.insert(2)
    test_cll.insertPostHead(3)
    test_cll.insertPostHead(4)
    test_cll.delete()
    test_cll.deleteHead()
    print(test_cll.length())
    test_cll.print()
