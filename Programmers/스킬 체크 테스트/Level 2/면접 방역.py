def manhattan_distance(r1, c1, r2, c2) -> int:
    return abs(r1 - r2) + abs(c1 - c2)


def is_valid_index(x, y) -> bool:
    return x >= 0 and x < 5 and y >= 0 and y < 5


def solution(places):
    directions = [
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1)
    ]

    def dfs(i, x, y) -> bool:
        nonlocal visited
        visited[i][x][y] = 1

        stack = []
        for direction_x, direction_y in directions:
            initial_x, initial_y = x + direction_x, y + direction_y
            if is_valid_index(initial_x, initial_y) and places[i][initial_x][initial_y] != "X":
                stack.append((initial_x, initial_y))

        while stack:
            current_x, current_y = stack.pop()

            visited[i][current_x][current_y] = 1

            if places[i][current_x][current_y] == "P":
                if manhattan_distance(x, y, current_x, current_y) <= 2:
                    return False

            for direction_x, direction_y in directions:
                next_x, next_y = current_x + direction_x, current_y + direction_y
                if is_valid_index(next_x, next_y) and places[i][next_x][next_y] != "X" and visited[i][next_x][next_y] == 0:
                    stack.append((next_x, next_y))

        return True

    def is_rules_satisfied(i) -> int:
        nonlocal visited
        for col in range(5):
            for row in range(5):
                if places[i][col][row] == "P" and visited[i][col][row] == 0 and dfs(i, col, row) is False:
                    return 0
        return 1

    answer = []
    visited = []

    for i in range(len(places)):
        visited.append(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]
            ]
        )
        answer.append(is_rules_satisfied(i))

    return answer


# [1, 0, 1, 1, 1]
places = [
    [
        "POOOP",
        "OXXOX",
        "OPXPX",
        "OOXOX",
        "POXXP"
    ],
    [
        "POOPX",
        "OXPXP",
        "PXXXO",
        "OXXXO",
        "OOOPP"
    ],
    [
        "PXOPX",
        "OXOXP",
        "OXPOX",
        "OXXOP",
        "PXPOX"
    ],
    [
        "OOOXX",
        "XOOOX",
        "OOOXX",
        "OXOOX",
        "OOOOO"
    ],
    [
        "PXPXP",
        "XPXPX",
        "PXPXP",
        "XPXPX",
        "PXPXP"
    ]
]
print(solution(places))
