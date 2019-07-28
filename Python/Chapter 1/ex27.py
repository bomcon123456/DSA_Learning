def awesomeFactors(n):
    k = 1
    other = []
    while k * k < n:
        if n % k == 0:
            yield k
            other.append(n // k)
        k += 1
    if k * k == n:
        yield k
    for i in range(0, len(other)):
        yield other[len(other) - 1 - i]


inp = int(input("Factor of: "))
print([i for i in awesomeFactors(inp)])
