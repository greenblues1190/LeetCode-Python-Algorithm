import sys
import heapq


def dijkstra(graph, start):
    # array of the shortest distances from initial vertex
    # initialize value for initial vertex as 0, and the rest as infinite.
    distances = {node: sys.maxsize for node in graph}
    distances[start] = 0

    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        current_distance, current_vertex  = heapq.heappop(queue)
        for next_vertex, weight in graph[current_vertex]:
            new_distance = current_distance + weight
            if new_distance < distances[next_vertex]:
                distances[next_vertex] = new_distance
                heapq.heappush(queue, (new_distance, next_vertex))

    return distances


graph = {
    1: [(2, 3), (3, 6), (4, 7)],
    2: [(1, 3), (3, 1)],
    3: [(1, 6), (2, 1), (4, 1)],
    4: [(1, 7), (3, 1)],
}

print(dijkstra(graph, 1))
