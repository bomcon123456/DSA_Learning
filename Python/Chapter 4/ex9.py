def findMinMax(arr, min, max, i):
    if i == len(arr):
        return (min, max)
    current = arr[i]
    if current < min:
        return findMinMax(arr, current, max, i + 1)
    elif current > max:
        return findMinMax(arr, min, current, i + 1)
    else:
        return findMinMax(arr, min, max, i + 1)


arr = [9, 8, 7, 6, 4, 6, 4, 3, 1, 0]
print(findMinMax(arr, arr[0], arr[0], 0))

