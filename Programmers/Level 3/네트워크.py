# https://programmers.co.kr/learn/courses/30/lessons/43162

# 네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다. 예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다. 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.

# 컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.

# 제한사항
# 컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
# 각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
# i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
# computer[i][i]는 항상 1입니다.


def solution(n, computers):
    def dfs(idx: int):
        next = []

        if computers[idx][idx] == 0:
            return

        # 방문한 컴퓨터의 연결 정보를 저장하고 0으로 변경
        for i in range(n):
            if computers[i][idx] == 1:
                next.append(i)
                computers[i][idx] = 0
                computers[idx][i] = 0

        # 연결된 컴퓨터 방문
        for next_idx in next:
            dfs(next_idx)

    answer = 0

    for idx in range(n):
        if computers[idx][idx] == 1:
            dfs(idx)
            answer += 1

    return answer
