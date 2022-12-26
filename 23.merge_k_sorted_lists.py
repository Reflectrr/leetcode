# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional, List


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # O(n*log(k))
        # n: total elements
        # k: total number of lists
        if not lists:
            return None
        mergingList = lists.copy()
        while len(mergingList) != 1:
            mergingList = []
            for index in range(0, len(lists), 2):
                list1 = lists[index]
                list2 = lists[index + 1] if len(lists) > index + 1 else None
                mergingList.append(self.mergeTwoLists(list1, list2))
            lists = mergingList.copy()
        return mergingList[0]


    def mergeTwoLists(self, list1, list2) -> Optional[ListNode]:
        sentinel = ListNode()
        curr = sentinel
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
                curr = curr.next
            else:
                curr.next = list2
                list2 = list2.next
                curr = curr.next
        if list1 or list2:
            curr.next = list2 if list2 else list1
        return sentinel.next
