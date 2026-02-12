"""
Docstring for dijkstra
Dijstra's algorithm is a greedy algorith that finds the shortest path from a given source node to all other nodes in a weighted graph
with non-negative edges

- weighted graph
- no negative weights
- single source -> all destinations
"""

import heapq


def dijkstra(graph, start):
    # initialze distances
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    # min-heap (priority queue)
    pq = [(0, start)]

    # process nodes
    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # ignore outdated distance
        if current_distance > distances[current_node]:
            continue

        for neighbour, weight in graph[current_node]:
            new_distance = current_distance + weight

            if new_distance < distances[neighbour]:
                distances[neighbour] = new_distance
                heapq.heappush(pq, (new_distance, neighbour))

    return distances


# graph definition
graph = {
    0: [(1, 1), (2, 4)],
    1: [(0, 1), (2, 2), (3, 5)],
    2: [(0, 4), (1, 2), (3, 1)],
    3: [(1, 5), (2, 1)],
}

# initantiate
start_node = 0
distances = dijkstra(graph, start_node)

# printing output
for node in distances:
    print(f"Shortest distances form {start_node} to {node} = {distances[node]}")
