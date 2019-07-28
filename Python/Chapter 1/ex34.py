sentence = "I will never spam my friends again"


def punished():
    count = 0
    import random

    arr = []
    for i in range(8):
        arr.append(random.randint(0, 99))

    for i in range(100):
        if i in arr:
            newSentence = list(sentence)
            index = random.randint(0, len(newSentence))
            value = " "
            while value == " ":
                index = random.randint(0, len(newSentence) - 1)
                value = ord(newSentence[index])
            changedLetter = value
            while changedLetter == value:
                changedLetter = random.randint(65, 123)
            newSentence[index] = chr(changedLetter)
            count += 1
            print(i + 1, ". ", "".join(newSentence), ".", sep="")
        else:
            print(i + 1, ". ", sentence, ".", sep="")


punished()

# print(ord("A"), ord("z"))
