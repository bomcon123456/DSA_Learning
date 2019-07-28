def norm(v, p=2):
    res = 0
    for each in v:
        res += each ** p
    res = res ** (1 / p)
    return res


data = [2, 6, 9]
print(norm(data, len(data)))
