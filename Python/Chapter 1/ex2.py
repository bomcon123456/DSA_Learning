def is_even(k):
    if k & 1 == 0:
        return True
    return False


a = int(input("Input a integer: "))
print(is_even(a))
