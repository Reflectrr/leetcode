class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for num in nums:
            index = abs(num) - 1
            if index < len(nums) and index >= 0:
                if nums[index] > 0:
                    nums[index] *= -1
                elif nums[index] == 0:
                    nums[index] = -(len(nums) + 1)

        for num in range(1, len(nums) + 1):
            if nums[num - 1] >= 0:
                return num
        return len(nums) + 1
