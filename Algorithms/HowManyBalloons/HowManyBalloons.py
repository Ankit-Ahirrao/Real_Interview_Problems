from collections import Counter

def solution(S):
    search_word = "BALLOON"
    frequency = Counter(S)
    target_fre = Counter(search_word)
    result = 0
    condition = lambda: all([frequency[char] >= target_fre[char] for char in target_fre])
    while condition():
        frequency = frequency - target_fre
        result += 1
    return result