def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def first_duplicate(arr):
    for i, num in enumerate(arr):
        swap(arr, i, num)
    for i, num in enumerate(arr):
        if num == arr[i-1]: return num