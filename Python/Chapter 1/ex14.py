def ex14(data):
    length = len(data)
    for i in range(0, length - 1):
        for j in range(i + 1, length):
            if data[i] != data[j] and (data[i] * data[j]) % 2 == 1:
                return True
    return False


data = [3, 4, 5, 6, 8, 10]
print(ex14(data))

