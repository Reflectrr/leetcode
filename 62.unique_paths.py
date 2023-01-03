class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memoization = [[0] * n for _ in range(m)]
        for i in range(m):
            memoization[i][0] = 1
        for i in range(n):
            memoization[0][i] = 1
        for y in range(1, m):
            for x in range(1, n):
                memoization[y][x] = memoization[y - 1][x] + memoization[y][x - 1]
        return memoization[m - 1][n - 1]
