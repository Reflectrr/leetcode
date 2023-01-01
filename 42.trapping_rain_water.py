class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        maxLeft, maxRight = height[left], height[right]
        res = 0
        while right > left:
            if maxLeft <= maxRight:
                left+=1
                res += max(maxLeft-height[left],0)
                if height[left]>maxLeft:
                    maxLeft = height[left]
            else:
                right-=1
                res += max(maxRight-height[right],0)
                if height[right]>maxRight:
                    maxRight = height[right]
        return res

