vows = "aeiou"


def more_vowels(string, consonants, vowels, i):
    if i == len(string):
        return consonants < vowels
    if string[i] in vows:
        return more_vowels(string, consonants, vowels + 1, i + 1)
    else:
        return more_vowels(string, consonants + 1, vowels, i + 1)


print(more_vowels("helloooo", 0, 0, 0))

