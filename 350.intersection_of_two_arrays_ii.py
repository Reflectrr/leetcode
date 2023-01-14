from collections import defaultdict


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        freq1, freq2 = defaultdict(int), defaultdict(int)
        res = []
        for num in nums1:
            freq1[num] += 1
        for num in nums2:
            freq2[num] += 1
        for num in freq1.keys():
            if num in freq2:
                freq = min(freq1[num], freq2[num])
                for _ in range(freq):
                    res.append(num)
        return res
