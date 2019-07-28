def is_multiple():
    n = int(input("Input n: "))
    m = int(input("Input m: "))
    if n % m == 0:
        return True
    else:
        return False


print(is_multiple())
