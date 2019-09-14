def palindrome(string, i):
    if i == len(string) // 2:
        return True
    if string[i] == string[-1 - i]:
        return palindrome(string, i + 1)
    else:
        return False


print(palindrome("bobob", 0))
