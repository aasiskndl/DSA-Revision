"""
A connected component of an undirected graph is the set of vertices such that every vertex in the set is
reachable from every other vertex in the same set, and no vertex is connected to any vertex outside the set.

Conected components can help to distinguish:
- if the graph is fully connected?
- how man seeparate networks exist?
- how many islands are there?
"""


def connected_components(graph):
    visited = set()
    components = []

    def dfs(node, component):
        visited.add(node)
        component.append(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                dfs(neighbour, component)

    for node in graph:
        if node not in visited:
            component = []
            dfs(node, component)
            components.append(component)
    return components


graph = {0: [1], 1: [0], 2: [3], 3: [2], 4: []}

components = connected_components(graph)

print("Number of connected components: ", len(components))
print("Connected components: ", components)
