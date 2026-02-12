# a cycle in graph is a path in which a vertex is reached again by following edges, without repeating edges, and the path lenght is greater than zero.

#example representation 

def has_cycle(graph):
    visited = set ()
    
    def dfs(node, parent):
        visited.add(node)
        
        for neighbour in graph[node]:
            if neighbour not in visited:
                if dfs(neighbour, node):
                    return True
                
            elif neighbour != parent:
                return True
            
        return False
    
    for node in graph:
        if node not in visited:
            if dfs(node, -1):
                return True
    return False

#graph with a cycle
'''
graph = {
    0: [1,2], 
    1: [0,2],
    2: [0,1],
    3: []
}
'''
# graph without cycle
graph = {
    0: [1],
    1: [0, 2],
    2: [1],
    3: []
}


if has_cycle(graph):
    print("Graph has a cycle")
    
else:
    print("Graph has no cycle")