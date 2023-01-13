from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        noFlip = set()

        def dfs(x, y):
            if (
                x >= 0
                and x < n
                and y >= 0
                and y < m
                and board[y][x] == "O"
                and (x, y) not in noFlip
            ):
                noFlip.add((x, y))
                dfs(x + 1, y)
                dfs(x - 1, y)
                dfs(x, y + 1)
                dfs(x, y - 1)

        # traverse through the borders and don't flip the connected component
        for index in range(m):
            if board[index][0] == "O":
                dfs(0, index)
            if board[index][n - 1] == "O":
                dfs(n - 1, index)
        for index in range(1, n):
            if board[0][index] == "O":
                dfs(index, 0)
            if board[m - 1][index] == "O":
                dfs(index, m - 1)

        for y in range(m):
            for x in range(n):
                if board[y][x] == "O" and (x, y) not in noFlip:
                    board[y][x] = "X"
        return
