from datetime import datetime
import time


def randomDate():
    import random

    currentNow = int(time.time())
    d = random.randint(currentNow - 1000000000, currentNow)
    return datetime.fromtimestamp(d).strftime("%Y-%m-%d")


test = [i for i in range(5, 101, 5)]

for n in test:
    arr = {}
    duplicated = []
    for i in range(n):
        birthday = randomDate()
        if birthday not in arr.keys():
            arr[birthday] = 1
        else:
            arr[birthday] += 1
            duplicated.append(birthday)
    # print(arr)
    print("Result for testcase: ", n)
    if len(duplicated) > 0:
        for i in duplicated:
            print(i, ": ", arr[i], sep="")
    else:
        print("No duplicated")

