class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return [-1,-1]
        left, right = 0, len(nums) - 1
        leftBound = (right - left) // 2
        res = []
        while right >= left:
            if nums[leftBound] == target:
                if leftBound - 1 < 0 or nums[leftBound - 1] != target:
                    res.append(leftBound)
                    break
                else:
                    right = leftBound - 1
            if nums[leftBound] < target:
                left = leftBound + 1
            else:
                right = leftBound - 1
            leftBound = (right - left) // 2 + left
        # look for the right bound
        left, right = leftBound, len(nums) - 1
        rightBound = (right - left) // 2 + left
        while right >= left:
            if nums[rightBound] == target:
                if rightBound + 1 >= len(nums) or nums[rightBound + 1] != target:
                    res.append(rightBound)
                    break
                else:
                    left = rightBound + 1
            elif nums[rightBound] < target:
                left = rightBound + 1
            else:
                right = rightBound - 1
            rightBound = (right - left) // 2 + left
        return res if len(res) == 2 else [-1, -1]
