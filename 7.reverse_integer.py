class Solution:
    def reverse(self, x: int) -> int:
        sign = [-1, 1][x > 0]
        reverseX = sign * int(str(abs(x))[::-1])
        return reverseX if reverseX >= -(2**31) and reverseX <= 2**31 - 1 else 0
