# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        MIN,MAX = -2**31, 2**31-1
        def helper(root, left, right) -> bool:
            if not root:
                return True
            elif root.val < left or root.val > right:
                return False
            else:
                return helper(root.left, left, root.val-1) and helper(
                    root.right, root.val+1, right
                )

        return helper(root, MIN, MAX)
