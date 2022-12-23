from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for index, num in enumerate(nums):
            if num > 0:
                break
            if index > 0 and num == nums[index - 1]:
                continue
            l, r = index + 1, len(nums) - 1
            target = -num
            while l < r:
                curr = nums[l] + nums[r]
                if curr == target:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and (nums) and nums[r] == nums[r + 1]:
                        r -= 1
                elif curr > target:
                    r -= 1
                else:
                    l += 1
        return res
