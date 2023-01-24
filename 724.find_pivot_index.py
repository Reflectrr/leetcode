class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        leftSum = 0
        total = sum(nums)
        for index in range(len(nums)):
            rightSum = total - nums[index] - leftSum
            if rightSum == leftSum:
                return index
            leftSum += nums[index]
        return -1
