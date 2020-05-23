class Node:
    def __init__(self, char):
        self.char = char
        self.child = {}
        self.frequency = 0

class Trie:
    def __init__(self):
        self.master = Node('master')
        
    def add(self, word):
        cur = self.master
        for char in word:
            if char not in cur.child: cur.child[char] = Node(char)
            cur = cur.child[char]
            cur.frequency += 1
            
    def get_unique_prefix(self, word):
        cur = self.master
        for i, char in enumerate(word):
            cur = cur.child[char]
            if cur.frequency == 1: return word[:i+1]        
            
class Solution:
    @staticmethod
    def prefix(A):
        trie = Trie()
        result_set = set()
        for word in A:
            trie.add(word)
        for word in A:
            prefix = trie.get_unique_prefix(word)
            result_set.add(prefix)
        return result_set

    
array = ['zebra', 'dogg', 'duck', 'dove']
set_out = Solution.prefix(array)
print(set_out)