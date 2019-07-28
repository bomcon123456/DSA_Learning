def minmax(data):
    min = 999999
    max = -999999
    for i in data:
        if i > max:
            max = i
        if i < min:
            min = i
    return min, max


data = input("Please enter array: ")
newData = data.split()
test = []
for i in newData:
    test.append(int(i))
print(minmax(test))
