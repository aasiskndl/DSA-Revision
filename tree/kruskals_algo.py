"""
Docstring for kruskals_algo
Kruskal's Algorithm(min spanning tree) is a greedy algorithm in graph theory that finds a minimum spanning tree for a connected, undirected, weighted graph
by sorting all edges by weight and adding them to the tree one by one if they dont form a cycle, ensuring the final tree connects all vertices with the minimum
total edge weight.

key points:
- use all vertices
- no cycles
- minimum total weight
- for v vertices => V - 1 edges

core idea of kruskal's algorithm is to pick the smallest weight edge that does not form a cycle.

steps:
1. sort all edges by weight
2. initialize union- find
3. for each edge (u,v,w):
    if u and v are in different sets:
        add edge to mst
        union(u,v)
4. stop when mst has V - 1 edges

"""


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
            return False

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True


def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)

    mst = []
    total_weight = 0

    for u, v, w in edges:
        if uf.union(u, v):
            mst.append((u, v, w))
            total_weight += w

    return mst, total_weight


edges = [(0, 1, 1), (1, 2, 2), (0, 2, 3), (1, 3, 4), (2, 3, 5)]

mst, weight = kruskal(4, edges)

print("MST edges: ", mst)
print("Total weights: ", weight)
