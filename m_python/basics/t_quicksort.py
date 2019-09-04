def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pvot = arr[len(arr) // 2]
    left = [x for x in arr if x < pvot]
    middle = [x for x in arr if x == pvot]
    right = [x for x in arr if x > pvot]

    return quicksort(left) + middle + quicksort(right)
