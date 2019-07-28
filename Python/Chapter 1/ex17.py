def scale(data, factor):
    for val in data:
        val *= factor


data = [1, 2, 3, 4, 5]
scale(data, 2)
print(data)

# No because we assign a new object with a value of factor * val, the actual element in the array still is val
