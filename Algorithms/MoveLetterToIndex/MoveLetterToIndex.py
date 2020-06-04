def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def move_letter(input1, input2):
    for i, v in enumerate(input1):
        swap(input1, i, input2[i])
        swap(input2, i, input2[i])
    return input1