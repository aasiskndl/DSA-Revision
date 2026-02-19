"""
A trie is also known as a prefix tree or digital tree, is a specilized tree based data structure used in computer science for effectively storing and retrieving strings.
Its key feature is that it organizes strings based on their shared prefixes, with each node representing a single character or symbol.

core concepts:
- nodes and edges: each node in a trie represents a single character or symbol, and the edge from a parent to a child corresponds to the character
- path as prefixes: the path from the root node to any other node forms a prefix of a word stored in the trie. the root typically represents an empty string
- end-of-word marker: nodes are typically marked with a special flag to indicate the path leading to it forms a complete, valid word that was inserted into the structure, not just a prefix
- shared prefixes: word sharing common prefixes such as "apple" and "apply", share the same initial nodes and edges, which make the trie memory-efficient for storing large dictonaries.
"""

