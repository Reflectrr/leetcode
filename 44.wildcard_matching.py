class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        memoization: dict[tuple[int, int], bool] = {}

        def isMatch(i: int, j: int) -> bool:
            if (i, j) in memoization:
                return False
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            if p[j] == "*":
                if isMatch(i, j + 1):
                    return True
                elif i < len(s) and isMatch(i + 1, j):
                    return True
            if i < len(s) and (s[i] == p[j] or p[j] == "?") and isMatch(i + 1, j + 1):
                return True
            memoization[(i, j)] = False
            return False

        return isMatch(0, 0)
