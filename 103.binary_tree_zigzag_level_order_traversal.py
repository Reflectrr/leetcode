# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        currStack, nextStack = [root], []
        level = 0
        curr = []
        res = []
        while currStack or nextStack:
            if not currStack:
                currStack = nextStack
                nextStack = []
                level += 1
                res.append(curr)
                curr = []
            item = currStack.pop(0)
            if not item:
                continue
            curr.append(item.val)
            if level % 2 == 0:
                nextStack.insert(0, item.left)
                nextStack.insert(0, item.right)
            else:
                nextStack.insert(0, item.right)
                nextStack.insert(0, item.left)
        return res
