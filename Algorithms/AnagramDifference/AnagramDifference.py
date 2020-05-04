from collections import Counter

def get_dif(word1, word2):
    if len(word1) != len(word2): return -1
    fre1 = Counter(word1)
    fre2 = Counter(word2)
    for k, v in fre2.items():
        if k not in fre1: fre1[k] = 0
        fre1[k] -= v
    ret = 0
    for k, v in fre1.items():
        ret += abs(v)
    return ret //2

def getMinimumDifference(a, b):
    ret = []
    for i in range(len(a)):
        difference = get_dif(a[i], b[i])
        ret.append(difference)
    return ret