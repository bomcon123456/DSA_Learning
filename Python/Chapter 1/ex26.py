def ex26(a, b, c):
    if a + b == c:
        return "a + b = c"
    elif a == b - c:
        return "a = b - c"
    elif a * b == c:
        return "a * b = c"


a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
print(ex26(a, b, c))

