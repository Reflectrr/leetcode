class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        mid = (right - left) // 2 + left
        while left <= right:
            square = mid*mid
            if square < x:
                left = mid+1
            elif square > x:
                right = mid-1
            else:
                return mid
            mid = (right - left) // 2 + left
        return mid
