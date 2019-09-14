def findLog(a):
    div = a // 2
    if div < 1:
        return 0
    return 1 + findLog(div)


while True:
    n = int(input("i = "))
    print(findLog(n))
