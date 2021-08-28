
# Merge two sorted linked lists into one

from Modules.SLL import SLL


def mergeSorted(a, b) -> SLL:
    result = SLL()
    temp = None
    a_ = a.getHeadNode()
    b_ = b.getHeadNode()

    return result


if __name__ == "__main__":
    test_data_a = SLL()
    test_data_b = SLL()
    for i in range(5):
        test_data_a.insert(i)
    for i in range(10, 13):
        test_data_a.insert(i)
    for i in range(34, 40):
        test_data_a.insert(i)
    for i in range(6, 10):
        test_data_b.insert(i)
    for i in range(14, 20):
        test_data_b.insert(i)
    for i in range(30, 33):
        test_data_b.insert(i)

    test_data_a.printList()
    test_data_b.printList()\

    merged = mergeSorted(test_data_a, test_data_b)
    merged.printList()
