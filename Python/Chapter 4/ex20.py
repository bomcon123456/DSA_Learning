# Time, Space: O(n)


def do(arr, l, r, i, x):
    if i == -1:
        return l + r
    if arr[i] <= x:
        l.append(arr[i])
    else:
        r.append(arr[i])
    return do(arr, l, r, i - 1, x)


def ex20(arr, x):
    left = []
    right = []
    return do(arr, left, right, len(arr) - 1, x)


arr = [11, 1, 9, 8, 6, 5, 12, 18, 48]
print(ex20(arr, 11))

