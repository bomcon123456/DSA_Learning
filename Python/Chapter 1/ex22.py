def sum(a, b):
    if len(a) != len(b):
        return
    length = len(a)
    result = []
    for i in range(0, length):
        result.append(a[i] * b[i])
    return result


print(sum((1, 2, 3, 4, 5), [0, 0, 0, 1, 1]))

