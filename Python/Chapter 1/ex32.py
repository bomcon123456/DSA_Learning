def ex32():
    c = ""
    res = 0
    plusNext = False
    while True:
        c = input()
        arr = c.split(" ")
        if len(arr) == 1:
            if c == "+":
                res = res
                plusNext = True
            elif c == "=":
                print(res)
                return res
            else:
                if plusNext:
                    res += float(c)
                else:
                    res = res * 10 + float(c)
        else:
            raise IOError("Unsupported operations")


ex32()
