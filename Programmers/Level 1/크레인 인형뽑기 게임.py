# https://programmers.co.kr/learn/courses/30/lessons/64061


def solution(board, moves):
    answer = 0
    N = len(board)
    lanes = [None]
    bucket = []

    # convert list to stack
    for lane in range(N):
        lanes.append([])
        pos = N - 1
        while pos >= 0 and board[pos][lane] != 0:
            lanes[lane + 1].append(board[pos][lane])
            pos -= 1

    # excute moves
    for move in moves:
        if not lanes[move]:
            continue

        item = lanes[move].pop()
        if item:
            if bucket and bucket[-1] == item:
                bucket.pop()
                answer += 2
            else:
                bucket.append(item)

    return answer


board = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 3],
    [0, 2, 5, 0, 1],
    [4, 2, 4, 4, 2],
    [3, 5, 1, 3, 1]
]

moves = [1, 5, 3, 5, 1, 2, 1, 4]

print(solution(board, moves))
