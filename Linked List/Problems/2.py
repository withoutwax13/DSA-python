# Remove duplicates in a sorted linked list

from Modules.SLL import SLL


def removeDuplicates(linkList) -> SLL:
    current = linkList.getHeadNode()
    prev = None
    while current.getNext() != None:
        if prev != None and prev.getData() == current.getData():
            prev.setNext(current.getNext())
            current = current.getNext()
        else:
            prev = current
            current = current.getNext()
    return linkList


if __name__ == "__main__":
    test_data = SLL()
    for i in range(13):
        test_data.insert(i+1)
    for i in range(13, 20):
        test_data.insert(i)
    for i in range(19, 25):
        test_data.insert(i)
    test_data.printList()
    clean_test_data = removeDuplicates(test_data)
    clean_test_data.printList()
