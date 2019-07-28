def inverse(data):
    length = len(data)
    for i in range(0, length // 2):
        temp = data[i]
        data[i] = data[length - 1 - i]
        data[length - 1 - i] = temp
    return data


data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(inverse(data))
