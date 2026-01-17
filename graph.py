# graph is a non-linear data structure consisting of finite set of vertices (nodes) and a set of edges that connect pairs of vertices.
# a graph can be represented as: G = (V, E)
# where V is the set fo vertices (nodes)
# E is the set of edges (connections betwn vertices)

# graphs can be used to model real world relationships (network, maps, social media)
# a graph does not have a single root
# nodes can have any number of connections
# cycles may or may not exist

# eg
from collections import deque

# graph definition ( it is also called adjacency list: it defines both the nodes and the connections between them. )
graph = {
    0: [1,2],
    1: [0,3,4],
    2: [0],
    3: [1],
    4: [1]
}

# bfs traversal in the graph

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    print("BFS traversal: ", end= " ")
    
    while queue:
        node = queue.popleft()
        print(node, end = " ")
        
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                
    print()
    

# dfs traversal in the graph 
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
        
    visited.add(start)
    print(start, end= " ")
    
    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)
        
print("Graph: ", graph)

bfs(graph, 0)

print("DFS traversal: ", end = " ")
dfs(graph, 0 ) 
print()   

