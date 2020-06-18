from collections import Counter

def begin_seq(search_list, words):
    result = []
    model = Counter(words)
    for beg, word in enumerate(search_list):
        end = beg+len(words)
        if word not in model: continue
        if end > len(search_list): break
        window_words = Counter([search_list[i] for i in range(beg, end)])
        print(beg, window_words)
        if window_words == model: result.append(beg)
    return result
