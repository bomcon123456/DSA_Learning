def product(a, b):
    if b > a:
        (a, b) = (b, a)
    if b == 1:
        return a
    return a + product(a, b - 1)


print(product(11, 15))

