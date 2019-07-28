def squares(n):
    sum = 0
    for i in range(n):
        sum += i * i
    return sum


n = int(input("Integer: "))
print(squares(n))
