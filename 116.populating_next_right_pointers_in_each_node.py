"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        root.next = None
        curr = root
        nextLevel = root.left
        while curr:
            if nextLevel:
                curr.left.next = curr.right
                curr.right.next = curr.next.left if curr.next else None
            curr = curr.next
            if not curr and nextLevel:
                curr = nextLevel
                nextLevel = curr.left
        return root
