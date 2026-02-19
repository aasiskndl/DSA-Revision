"""
A trie is also known as a prefix tree or digital tree, is a specilized tree based data structure used in computer science for effectively storing and retrieving strings.
Its key feature is that it organizes strings based on their shared prefixes, with each node representing a single character or symbol.

core concepts:
- nodes and edges: each node in a trie represents a single character or symbol, and the edge from a parent to a child corresponds to the character
- path as prefixes: the path from the root node to any other node forms a prefix of a word stored in the trie. the root typically represents an empty string
- end-of-word marker: nodes are typically marked with a special flag to indicate the path leading to it forms a complete, valid word that was inserted into the structure, not just a prefix
- shared prefixes: word sharing common prefixes such as "apple" and "apply", share the same initial nodes and edges, which make the trie memory-efficient for storing large dictonaries.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
                
            node = node.children[ch]
            
        node.is_end = True
    
    # search full word
    def search(self, word):
        node = self.root
        
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
            
        return node.is_end
    
    # check prefix
    def startsWith(self, prefix):
        node = self.root
        
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
            
        return True

trie = Trie()

trie.insert("cat")
trie.insert("car")
trie.insert("dog")

print(trie.search("cat"))
print(trie.search("ca"))
print(trie.startsWith("ca"))
