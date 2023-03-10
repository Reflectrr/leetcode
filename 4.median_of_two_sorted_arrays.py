class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        totalLen = len(nums1)+len(nums2)
        if totalLen % 2 == 1:
            return self.kth(nums1,nums2,totalLen//2)
        else:
            return (self.kth(nums1,nums2,totalLen//2)+self.kth(nums1, nums2, totalLen//2-1))/2


    def kth(self, a:List[int],b:List[int],k:int):
        if not a: return b[k]
        if not b: return a[k]
        ia, ib = len(a)//2, len(b)//2
        ma, mb = a[ia], b[ib]

        if ia + ib < k:
            if ma > mb:
                return self.kth(a,b[ib+1:], k-ib-1)
            else: 
                return self.kth(a[ia+1:], b, k-ia-1)
        else:
            if ma>mb:
                return self.kth(a[:ia], b, k)
            else:
                return self.kth(a, b[:ib], k)
