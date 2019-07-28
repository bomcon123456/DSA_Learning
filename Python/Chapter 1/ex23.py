def insert(data, index, value):
    length = len(data)
    if index >= length:
        raise IndexError("Don't try buffer overflow attacks in Python!")
    data[index] = value


data = [1, 2, 3, 4, 5, 6, 7]
insert(data, 5, 3)
print(data)
