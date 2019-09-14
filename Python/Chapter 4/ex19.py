def weird_sort(arr, i):
    if i < 0:
        return
    if arr[i] % 2 == 0:
        arr.insert(0, arr.pop(i))
    weird_sort(arr, i - 1)


arr = [4, 67, 3, 54, 6, 7, 8, 3, 1, 2, 4, 6, 7]
weird_sort(arr, len(arr) - 1)
print(arr)
