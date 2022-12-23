class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        res = 0
        while right > left:
            width = right - left
            shorterSide = min(height[right], height[left])
            res = max(res, width * shorterSide)
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return res
