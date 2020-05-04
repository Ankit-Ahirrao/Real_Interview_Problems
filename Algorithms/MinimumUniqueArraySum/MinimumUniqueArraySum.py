def getMinimumUniqueSum(arr):
    mem = set()
    for i in range(len(arr)):
        if arr[i] not in mem:
            mem.add(arr[i])
        else:
            while (arr[i] in mem):
                arr[i] += 1
            mem.add(arr[i])
    return sum(arr)
