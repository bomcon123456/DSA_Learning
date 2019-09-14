def power(x, n):
    if n == 0:
        return 1
    i = 1
    res = x
    while i < n:
        print("lol")
        if i * 2 < n:
            res *= res
            i *= 2
        else:
            res *= x
            i += 1
    return res


print(power(2, 11))
