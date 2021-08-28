def isSorted(array):
    if len(array) == 1:
        return True
    return array[0] < array[1] and isSorted(array[1:])


print(isSorted([1, 2, 3, 4, 6, 5]))  # false
