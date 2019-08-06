def findMinMax(arr):
    big = []
    small = []
    max = min = arr[0]
    for i in range(1, len(arr) + 1, 2):
        if i == len(arr):
            big.append(arr[i - 1])
            break
        larger, smaller = (
            (arr[i - 1], arr[i]) if arr[i - 1] >= arr[i] else (arr[i], arr[i - 1])
        )
        big.append(larger)
        small.append(smaller)
    for i in range(0, len(big)):
        if big[i] > max:
            max = big[i]
    for i in range(0, len(small)):
        if small[i] < min:
            min = small[i]
    return max, min
