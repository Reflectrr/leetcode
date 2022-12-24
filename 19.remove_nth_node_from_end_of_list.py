# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sentinel = ListNode(-1, head)
        front, back = head, sentinel
        for i in range(n):
            if not front:
                return head
            front = front.next
        while front:
            front = front.next
            back = back.next
        back.next = back.next.next
        return sentinel.next
