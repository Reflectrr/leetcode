class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memoization: dict[tuple[int, int], bool] = {}

        def dfs(i: int, j: int) -> bool:
            if (i, j) in memoization:
                return memoization[(i, j)]

            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False

            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if j + 1 < len(p) and p[j + 1] == "*":
                if match and dfs(i + 1, j):
                    return True
                if dfs(i, j + 2):
                    return True
            if match and dfs(i + 1, j + 1):
                return True
            memoization[(i, j)] = False
            return False

        return dfs(0, 0)
