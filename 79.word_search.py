from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = set()
        for char in word:
            if char not in sum(board, []):
                return False

        def dfs(row, col, word):
            if (row, col) in visited:
                return False
            # check if finished searching
            if word == "":
                return True
            searchChar = word[0]
            visited.add((row, col))
            if (
                (
                    row - 1 >= 0
                    and board[row - 1][col] == searchChar
                    and dfs(row - 1, col, word[1:])
                )
                or (
                    row + 1 < m
                    and board[row + 1][col] == searchChar
                    and dfs(row + 1, col, word[1:])
                )
                or (
                    col - 1 >= 0
                    and board[row][col - 1] == searchChar
                    and dfs(row, col - 1, word[1:])
                )
                or (
                    col + 1 < n
                    and board[row][col + 1] == searchChar
                    and dfs(row, col + 1, word[1:])
                )
            ):
                return True
            visited.remove((row, col))
            return False

        for row in range(m):
            for col in range(n):
                if board[row][col] == word[0] and dfs(row, col, word[1:]):
                    return True
        return False
