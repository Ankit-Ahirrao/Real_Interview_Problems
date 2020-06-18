def set_state(arr, l, r, value):
    for i in range(l, r):
        arr[i] = value

def alloc(arr, size, memo):
    if size <= 0: return -1
    left = 0
    for right in range(len(arr)):
        if arr[left]: left = right
        if not arr[right] and right-left+1 == size:
            memo.append((left, right+1))
            set_state(arr, left, right+1, 1)
            return left
        if arr[right]: left = right
    return -1
    
def erase(arr, block_id, memo):
    if block_id-1 >= len(memo): return -1
    lo, hi = memo[block_id-1]
    set_state(arr, lo, hi, 0)
    return hi-lo

def memoryAllocator(a, queries):
    ret, memo = [], []
    for action, status in queries:
        if action == 0:
            ret.append(alloc(a, status, memo))
        if action == 1:
            ret.append(erase(a, status, memo))
    return ret