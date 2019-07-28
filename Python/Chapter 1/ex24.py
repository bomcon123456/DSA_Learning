vowels = ["a", "e", "i", "o", "u"]


def countVowels(string):
    count = 0
    for i in string:
        if i in vowels:
            count += 1
    return count


print(countVowels("Keemochi is my kee"))

