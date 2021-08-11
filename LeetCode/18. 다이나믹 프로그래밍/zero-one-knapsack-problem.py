from typing import List, Tuple


def zero_one_knapsack(cargo: List[Tuple[int]], capacity: int) -> int:
    pack = []

    for i in range(len(cargo) + 1):
        pack.append([])
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                pack[i].append(0)
            elif cargo[i - 1][1] <= j:
                pack[i].append(
                    max(
                        cargo[i - 1][0] + pack[i - 1][j - cargo[i - 1][1]],
                        pack[i - 1][j]
                    )
                )
            else:
                pack[i].append(pack[i - 1][j])

    return pack[-1][-1]


cargo = [
    (4, 12),
    (2, 1),
    (10, 4),
    (1, 1),
    (2, 2),
]
capacity = 15

print(zero_one_knapsack(cargo, capacity))
