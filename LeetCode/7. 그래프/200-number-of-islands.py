# https://leetcode.com/problems/number-of-islands/

# Given an m x n 2D binary grid grid which represents a map
# of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by
# connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.


from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x: int, y: int) -> None:
            # mark the current vertex as visited (0)
            grid[x][y] = 0

            # Search vertically/horizontally adjacent vertex
            for dir_x, dir_y in direction:
                next_x, next_y = x + dir_x, y + dir_y
                if next_x < col_length and next_y < row_length and next_x >= 0 and next_y >= 0 and grid[next_x][next_y] == "1":
                    dfs(next_x, next_y)

        direction = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1],
        ]
        col_length, row_length = len(grid), len(grid[0])
        island_count = 0

        for i, col in enumerate(grid):
            for j, is_land in enumerate(col):
                if is_land == "1":
                    dfs(i, j)
                    island_count += 1

        return island_count


# test case
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

obj = Solution()
print(obj.numIslands(grid))
