def subset(arr):
    if len(arr) == 1:
        return arr
    result = []
    pop_one = arr.pop(0)
    result.append([pop_one])
    lower = subset(arr)
    for each in lower:
        if not isinstance(each, list):
            result.insert(0, [each])
            result.insert(0, [pop_one, each])
        else:
            test = each.copy()
            result.insert(0, test)
            each.insert(0, pop_one)
            result.insert(0, each)
    return result


def find_subset(arr):
    newArr = arr.copy()
    return subset(newArr)


# Credit to kosbie.net
def find_subset_better(input):
    if len(input) == 0:
        return [[]]
    else:
        main_subset = []
        for small_subset in find_subset_better(input[1:]):
            main_subset += [small_subset]
            main_subset += [[input[0]] + small_subset]
        return main_subset


arr = [1, 2, 3, 4]
a = find_subset(arr)
b = find_subset_better(arr)

for each in a:
    if len(each) != len(arr):
        print(each)

for each in b:
    if len(each) != len(arr):
        print(each)
