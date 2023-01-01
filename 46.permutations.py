class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==1:
            return [nums.copy()]
        res = []

        for _ in range(len(nums)):
            val = nums.pop(0)
            perm = self.permute(nums)
            for array in perm:
                array.append(val)
                res.append(array)
            nums.append(val)

        return res
