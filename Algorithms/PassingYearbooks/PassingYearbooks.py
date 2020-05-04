def group(arr, i):
    count = 0
    while arr[i] != 0:
        count += 1
        arr[i], i = 0, arr[i]-1

def findSignatureCounts (arr):
    singature_count = 0
    for i in range(len(arr)):
        if arr[i] == 0: continue
        singature_count += group(arr, i)**2
    print(singature_count)
    return singature_count