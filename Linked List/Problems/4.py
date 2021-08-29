
# Merge two sorted linked lists into one

from Modules.SLL import SLL


def mergeSorted(a, b) -> SLL:

    def merge(arrA, arrB):
        result = [arrA + arrB]
        for i, data in enumerate(result):
            for j in range(i, len(result)):
                current = result[j]
                if data > current:
                    temp = data
                    result[i] = current
                    result[j] = temp
        return result

    def split(arr):
        if len(arr) == 1:
            return arr
        else:
            import math
            midP = math.ceil(len(arr)/2)
            arrA = [i for i in range(midP)]
            arrB = [i for i in range(midP, len(arr))]
            return split(merge(arrA, arrB))

    a_, b_, a_data, b_data = a.getHeadNode(), b.getHeadNode(), [], []
    while a_.getNext() != None:
        a_data.append(a_.getData())
        a_ = a_.getNext()
    while b_.getNext() != None:
        b_data.append(b_.getData())
        b_ = b_.getNext()
    result, retResult = split(a_data + b_data), SLL()
    for each in result:
        retResult.insert(each)
    return retResult


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
    test_data_b.printList()

    merged = mergeSorted(test_data_a, test_data_b)
    merged.printList()
