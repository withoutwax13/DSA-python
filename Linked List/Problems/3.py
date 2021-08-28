# Split a linked list into two lists where each list contains alternating elements from it

from Modules.SLL import SLL


def splitIntoTwo(linkList) -> list:
    left = True
    left_list = SLL()
    right_list = SLL()

    current = linkList.getHeadNode()
    while current.getNext() != None:
        if left:
            left_list.insert(current.getData())
        else:
            right_list.insert(current.getData())
        current = current.getNext()
        left = not left

    return [left_list, right_list]


if __name__ == "__main__":
    test_data = SLL()
    for i in range(24):
        test_data.insert(i)
    test_data.printList()
    arranged_data = splitIntoTwo(test_data)
    for i in arranged_data:
        i.printList()
