import collections

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}


# DFS
def reculsive_dfs(graph: dict, start_vertex: int, discovered=[]) -> list:
    discovered.append(start_vertex)
    for next_vertex in graph[start_vertex]:
        if next_vertex not in discovered:
            discovered = reculsive_dfs(graph, next_vertex, discovered)
    return discovered


def iterative_dfs(graph: dict, start_vertex: int) -> list:
    discovered = []
    stack = []
    stack.append(start_vertex)
    while stack:
        vertex = stack.pop()
        if vertex not in discovered:
            discovered.append(vertex)
            for next_vertex in graph[vertex]:
                stack.append(next_vertex)
    return discovered


# BFS
def BFS(graph: dict, start_vertex: int):
    discovered = []
    queue = collections.deque()
    queue.append(start_vertex)
    while queue:
        vertex = queue.popleft()
        if vertex not in discovered:
            discovered.append(vertex)
            for next_vertex in graph[vertex]:
                queue.append(next_vertex)
    return discovered


print("Reculsive DFS:", reculsive_dfs(graph, 1))
print("Iterative DFS:", iterative_dfs(graph, 1))
print("BFS:", BFS(graph, 1))
