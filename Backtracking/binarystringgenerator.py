def appendAtFront(x, L):
    return [x + element for element in L]


def bitstrings(n):
    if n == 0:
        return []
    elif n == 1:
        return ["0", "1"]
    else:
        return appendAtFront("0", bitstrings(n-1)) + appendAtFront("1", bitstrings(n-1))


if __name__ == "__main__":
    print(bitstrings(4))
