words = input("List of words: ")
words = words.split(" ")

myDict = {}
for word in words:
    if word not in myDict.keys():
        myDict[word] = 1
    else:
        myDict[word] += 1

# print(myDict)

print("\n".join("{}: \t{}".format(k, v) for k, v in myDict.items()))
