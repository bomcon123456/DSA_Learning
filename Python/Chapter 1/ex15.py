def ex15(data):
    length = len(data)
    for i in range(0, length - 1):
        for j in range(i + 1, length):
            if data[i] == data[j]:
                return False
    return True


data = [2, 2, 5, 6, 8, 10]
print(ex15(data))

