def removePunc(myString):
    import string

    table = str.maketrans({key: None for key in string.punctuation})
    print(table)
    # new_s = myString.translate(table)  # Output: string without punctuation
    # return new_s


test = "Let's try, mate"
# removePunc(test)
print(removePunc(test))

