def toInt(string, n):
    if n < 0:
        return
    if n == 0:
        return int(string[n], 10)
    return toInt(string, n - 1) * 10 + int(string[n])


a = "53453534534"
print(toInt("53453534534", len(a) - 1))

