def cheatedEx29():
    import itertools

    arr = ["c", "a", "t", "d", "o", "g"]
    perm = itertools.permutations(arr)
    for c in perm:
        a = "".join(c)
        yield a


def recurse(arr):
    if len(arr) <= 1:
        return arr
    res = []
    for c in arr:
        newArr = arr.copy()
        newArr.remove(c)
        lol = recurse(newArr)
        for k in lol:
            res.append(c + k)
    return res


res = recurse(["c", "a", "t", "d", "o", "g"])
print(len(res))

lent = 0
for i in cheatedEx29():
    lent += 1
print(lent)
