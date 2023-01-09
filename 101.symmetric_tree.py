# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def helper(left, right)->bool:
            if not left and not right:
                return True
            elif not left and right or not right and left:
                return False
            elif left.val == right.val:
                return helper(left.left, right.right) and helper(left.right, right.left)
            return False
        return helper(root, root)

