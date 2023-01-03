class Solution:
    def climbStairs(self, n: int) -> int:
        a, b, res = 1, 1, 0
        if n == 1:
            return 1
        for _ in range(n - 1):
            res = a + b
            b = a
            a = res
        return res
