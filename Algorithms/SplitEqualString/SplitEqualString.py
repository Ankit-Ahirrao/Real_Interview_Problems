from collections import Counter
def countb(S, count):
    target = count //3
    cur_count = 0
    a_ind = []
    for i,char in enumerate(S):
        if char == 'a': cur_count += 1
        if cur_count == target:
            a_ind.append(i)
            cur_count = 0
    return a_ind[1]-a_ind[0]-1, a_ind[2]-a_ind[1]-1

def count_frequency(S, target):
    fre = Counter(S)
    return 0 if target not in fre else fre[target]

def solution(S):
    part = 3
    if not S: return 0
    a_count = count_frequency(S, 'a')
    if a_count == 0: return len(S)+1
    if (a_count%part) != 0: return 0
    left, right = countb(S, a_count)
    return (left+1)*(right+1)