'''
UNion find efficientl keeos track of which element belong to the same group(set)

in graph terms:
- are two nodes connected?
- how many separate groups exist?
- what happens if we connect two nodes?
Unlike dfs/bfs, it works dynamically (edges can be added anytime)

two main operations:
- find(x): finds the root(leader) of the element
- union(x,y): merges the set containing x and y
'''


