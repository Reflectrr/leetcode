# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # slow at the middle, start reversing
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        front = head
        back = prev
        while front and back:
            if front.val != back.val:
                return False
            front = front.next
            back = back.next
        return True
