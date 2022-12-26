class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniqueIndex = 1  # index to place next unique value
        for index in range(1, len(nums)):
            # iterate through the array 
            # keep placing unique values at above index
            if nums[index] != nums[index - 1]:
                nums[uniqueIndex] = nums[index]
                uniqueIndex += 1
        return uniqueIndex
