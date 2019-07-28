def ex30(a):
    count = 0
    while a >= 2:
        a = a // 2
        count += 1
    return count


inp = int(input("Input: "))
print(ex30(inp))
