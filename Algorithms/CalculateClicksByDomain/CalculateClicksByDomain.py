class Node:
    def __init__(self, domain):
        self.children = {}
        self.frequency = 0
        self.domain = domain
            
    def print_all(self, pre = []):
        full_domain = '.'.join([self.domain]+pre)
        print(full_domain + ':' + str(self.frequency))
        for domain in self.children:
            self.children[domain].print_all([self.domain]+pre)

class Trie:
    def __init__(self):
        self.master = Node('')
    
    def add(self, fre, domain_arr):
        cur = self.master
        for domain in domain_arr:
            if domain not in cur.children:
                cur.children[domain] = Node(domain)
            cur = cur.children[domain]
            cur.frequency += fre
            
    def print_all(self):
        for child in self.master.children:
            self.master.children[child].print_all([])
            
def destructure(arr):
    for string in arr:
        fre, whole_domain = string.split(',')
        sub_domains = []
        for sub in whole_domain.split('.')[::-1]:
            sub_domains.append(sub)
        yield int(fre), sub_domains
            
def calculateClicksByDomain(arr):
    trie = Trie()
    for count, domains in destructure(arr):
        trie.add(count, domains)
    trie.print_all()