def checkValueIsUnique(S, currentStep, currentValue):
    if currentStep == len(S):
        return True
    if S[currentStep] == currentValue:
        return False
    return checkValueIsUnique(S, currentStep + 1, currentValue)


def unique3(S, i):
    if i == len(S):
        return True
    if checkValueIsUnique(S, i + 1, S[i]):
        return unique3(S, i + 1)
    return False


print(unique3([1, 4, 3, 4], 0))

