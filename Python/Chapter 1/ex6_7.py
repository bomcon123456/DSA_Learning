n = int(input("Integer: "))
print(sum([k * k if k % 2 == 1 else 0 for k in range(n)]))

