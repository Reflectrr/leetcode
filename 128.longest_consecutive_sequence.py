class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        res = 0
        numSet = set(nums)
        for num in numSet:
            if num -1 not in numSet:
                length = 1
                while num + 1 in numSet:
                    num = num + 1
                    length += 1
                if length > res:
                    res = length
        return res



