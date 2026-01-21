'''
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

'''