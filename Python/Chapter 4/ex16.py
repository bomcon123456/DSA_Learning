def reverse(i, string):
    if i == len(string):
        return
    reverse(i + 1, string)
    print(string[i], end="")


reverse(0, "pots&pans")
