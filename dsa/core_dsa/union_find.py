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

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return
        
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
            
uf = UnionFind(5)
uf.union(0,1)
uf.union(1,2)
uf.union(3,4)

print(uf.find(0) == uf.find(2))
print(uf.find(0) == uf.find(4))

