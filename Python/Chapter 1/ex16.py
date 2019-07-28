def scale(data, factor):
    for j in range(len(data)):
        data[j] *= factor


data = [1, 2, 3, 4, 5]
scale(data, 2)
print(data)

# Because the element in that index will be another (newly-created) object which is immuatable too
