import platform  # For getting the operating system name
import subprocess  # For executing a shell command


def clear_screen():
    """
    Clears the terminal screen.
    """

    # Clear command as function of OS
    command = "cls" if platform.system().lower() == "windows" else "clear"

    # Action
    return subprocess.call(command) == 0


inputArr = {
    "1": "NUMBER",
    "2": "NUMBER",
    "3": "NUMBER",
    "4": "NUMBER",
    "5": "NUMBER",
    "6": "NUMBER",
    "7": "NUMBER",
    "8": "NUMBER",
    "9": "NUMBER",
    "+": "OPs",
    "-": "OPs",
    "*": "OPs",
    "/": "OPs",
}


def calculateChar(a, b, ops):
    res = 0
    a = float(a)
    b = float(b)
    if ops == "+":
        res = a + b
    elif ops == "-":
        res = a - b
    elif ops == "*":
        res = a * b
    elif ops == "/":
        res = a / b
    return res


globalResult = "WHAT"


def setGlobal(res):
    global globalResult
    globalResult = res


def calculate(arr):
    operators = []
    numbers = []
    popNext = False
    wasNumber = False
    for c in arr:
        if inputArr[c] == "OPs":
            wasNumber = False
            operators.append(c)
            if c == "*" or c == "/":
                popNext = True
        else:
            if wasNumber:
                old = numbers.pop()
                new = old + c
                numbers.append(new)
            else:
                numbers.append(c)
                wasNumber = True
            if popNext:
                a = numbers.pop()
                b = numbers.pop()
                op = operators.pop()
                new = calculateChar(b, a, op)
                numbers.append(new)
                popNext = False
                wasNumber = False

    while len(operators) > 0:
        op = operators.pop()
        if len(numbers) >= 2:
            a = numbers.pop()
            b = numbers.pop()
            numbers.append(calculateChar(b, a, op))
        else:
            break

    res = numbers.pop()
    setGlobal(res)
    return res


def calculatorInput():
    currentInput = []

    c = ""
    while c != "x":
        clear_screen()
        if globalResult == "WHAT":
            for c in currentInput:
                print(c, end=" ")
            print()
        else:
            print("RESULT:", globalResult)
            setGlobal("WHAT")
        print("Press 1 for input 1")
        print("Press 2 for input 2")
        print("Press 3 for input 3")
        print("Press 4 for input 4")
        print("Press 5 for input 5")
        print("Press 6 for input 6")
        print("Press 7 for input 7")
        print("Press 8 for input 8")
        print("Press 9 for input 9")
        print("Press + for input +")
        print("Press - for input -")
        print("Press * for input *")
        print("Press / for input /")
        print("Press = for input =")
        print("Press x for input EXIT")
        print("Press r for input RESET")
        print("Press d for input DELETE")

        c = input("Press: ")
        if c == "d":
            currentInput.pop()
        elif c == "r":
            currentInput = []
        elif c == "=":
            calculate(currentInput)
            currentInput = []
        else:
            currentInput.append(c)


calculatorInput()
# calculate(
#     [
#         "1",
#         "+",
#         "2",
#         "*",
#         "3",
#         "+",
#         "(",
#         "1",
#         "2",
#         "/",
#         "4",
#         "+",
#         "7",
#         "/",
#         "3",
#         "+",
#         "2",
#         "*",
#         "(",
#         "1",
#         "+",
#         "2",
#         ")",
#         ")",
#     ]
# )
# calculate(["(", "1", "+", "2", ")", "*", "3", "+", "(", "1", "2", "/", "4", ")"])
# calculate(arr)
