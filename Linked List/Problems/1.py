# Implement stacks using linked list

from Modules.SLL import SLL


class Stack(object):

    def __init__(self):
        self.container = SLL()

    def push(self, data) -> None:
        self.container.insert(data)

    def pop(self) -> int:
        toReturn = self.container.getHeadData()
        self.container.deleteAtBegin()
        return toReturn

    def top(self) -> int:
        return self.container.getHeadData()

    def length(self) -> int:
        return self.container.length()

    def print(self) -> None:
        self.container.printList()


if __name__ == "__main__":
    sample = Stack()
    sample.push(1)
    sample.push(2)
    sample.print()
    print(sample.pop())
    sample.print()
