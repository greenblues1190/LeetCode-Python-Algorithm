# https://programmers.co.kr/learn/courses/30/lessons/49189

# n개의 노드가 있는 그래프가 있습니다. 각 노드는 1부터 n까지 번호가 적혀있습니다. 1번 노드에서 가장 멀리 떨어진 노드의 갯수를
# 구하려고 합니다. 가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미합니다.

# 노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때, 1번 노드로부터 가장 멀리 떨어진 노드가 몇
# 개인지를 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 노드의 개수 n은 2 이상 20,000 이하입니다.
# 간선은 양방향이며 총 1개 이상 50,000개 이하의 간선이 있습니다.
# vertex 배열 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다는 의미입니다.


import collections
import sys
import heapq


def dijkstra(n, graph):
    distances = {node: sys.maxsize for node in range(1, n + 1)}
    distances[1] = 0

    queue = []
    heapq.heappush(queue, (0, 1))

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        for next_vertex in graph[current_vertex]:
            new_distance = current_distance + 1
            if new_distance < distances[next_vertex]:
                distances[next_vertex] = new_distance
                heapq.heappush(queue, (new_distance, next_vertex))

    return distances


def solution(n, edge):
    answer = 0

    # hash를 이용해 edge를 graph로 변환
    graph = collections.defaultdict(list)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    # 다익스트라 알고리즘으로 1번 노드에서 각 노드까지의 최단 거리 리스트를 구하여 그 중 최댓값에 해당하는 거리 개수를 반환
    distances = dijkstra(n, graph)
    max_d = max(distances.values())
    for d in distances.values():
        if d == max_d:
            answer += 1

    return answer
