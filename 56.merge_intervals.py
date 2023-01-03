from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sortedIntervals = sorted(intervals, key=lambda i: i[0])
        res = []
        for interval in sortedIntervals:
            start = interval[0]
            # update the interval 
            if res and start >= res[-1][0] and start <= res[-1][1]:
                res[-1][1] = max(interval[1], res[-1][1])
            else:
                res.append(interval)
        return res
