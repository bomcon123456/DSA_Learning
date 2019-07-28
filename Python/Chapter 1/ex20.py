def swap(data, i, j):
    temp = data[i]
    data[i] = data[j]
    data[j] = temp


def shuffle(data):
    length = len(data)
    import random

    for i in range(0, length):
        j = random.randint(0, length - 1)
        swap(data, i, j)


data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
shuffle(data)
print(data)
