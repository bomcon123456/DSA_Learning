lines = []
while True:
    try:
        lines.append(input("Input: "))
    except EOFError:
        print()
        for i in range(0, len(lines)):
            print(lines[len(lines) - 1 - i])
        raise

