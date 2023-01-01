class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res = nums[0]
        ptr = 0
        curr = 0
        while ptr < len(nums):
            curr += nums[ptr]
            if nums[ptr]>curr:
                curr = nums[ptr]
            if curr > res:
                res = curr
            ptr += 1
        return res
