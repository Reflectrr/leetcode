# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        signal = TreeNode(val=1001)
        queue = [root, signal]
        res = []
        curr = []

        while queue:
            item = queue.pop(0)
            if item == signal:
                if queue:
                    queue.append(signal)
                res.append(curr)
                curr = []
            else:
                curr.append(item.val)
                if item.left:
                    queue.append(item.left)
                if item.right:
                    queue.append(item.right)
        return res
