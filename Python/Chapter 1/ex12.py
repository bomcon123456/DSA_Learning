def choice(data):
    import random

    i = random.randrange(0, len(data))
    return data[i]


data = [1, 2, 3, 4, 5, 6, 7, 8, 10, 12312]
print(choice(data))
