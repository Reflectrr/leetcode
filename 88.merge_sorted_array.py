class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr1, ptr2 = m - 1, n - 1
        curr = m + n - 1
        while curr > ptr1:
            if ptr1 >= 0 and nums1[ptr1] > nums2[ptr2]:
                nums1[curr] = nums1[ptr1]
                nums1[ptr1] = 0
                ptr1 -= 1
            else:
                nums1[curr] = nums2[ptr2]
                ptr2 -= 1
            curr -= 1
        return
