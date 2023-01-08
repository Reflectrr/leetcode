class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        subset = []
        def dfs(index):
            if index >= len(nums):
                res.append(subset.copy())
                return
            dfs(index+1)
            subset.append(nums[index])
            dfs(index+1)
            subset.pop()
        dfs(0)
        return res

