# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = -2**31
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(root)->int:
            if not root:
                return -2**31
            leftMax = helper(root.left)
            rightMax = helper(root.right)
            maxVal = max(
                root.val,
                root.val + leftMax,
                root.val + rightMax,
                root.val + leftMax + rightMax,
            )
            if maxVal > self.res:
                self.res = maxVal
            return max(root.val, root.val + leftMax, root.val + rightMax)
        helper(root)
        return self.res
