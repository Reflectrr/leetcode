class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        swapStartSearch = 0
        for index in range(len(nums)):
            if nums[index] == 0:
                noswap = True
                swapStartSearch = max(index+1, swapStartSearch)
                for nonZeroIdx in range(swapStartSearch, len(nums)):
                    if nums[nonZeroIdx] != 0:
                        nums[index]=nums[nonZeroIdx]
                        nums[nonZeroIdx]=0
                        swapStartSearch = nonZeroIdx
                        noswap = False
                        break
                if noswap:
                    return
        return 
