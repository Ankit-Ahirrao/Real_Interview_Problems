from collections import defaultdict
    
class Node:
    def __init__(self):
        self.children = defaultdict(lambda: Node())
        self.indices = set()
    
class Trie:
    def __init__(self):
        self.master = Node()
    
    def add(self, ind, word):
        cur = self.master
        for char in word:
            cur = cur.children[char]
        cur.indices.add(ind)

    def search(self, query):
        cur = self.master
        for char in query:
            cur = cur.children[char]
        return cur.indices
    
def build_trie(strings):
    trie = Trie()
    for i, sentences in enumerate(strings):
        words = sentences.split(' ')
        for word in words:
            trie.add(i, word)
    return trie

# Assuming search query contain only 1 word here
def search_engine(strings, search_query):
    trie = build_trie(strings)
    all_indices = trie.search(search_query)
    return [strings[i] for i in all_indices]

# Search query contain multiple words
def search_engine(strings, search_query):
    trie = build_trie(strings)
    ret = set([i for i in range(len(strings))])
    for word in search_query.split(' '):
        ret = ret & trie.search(word)
    return [strings[i] for i in ret]