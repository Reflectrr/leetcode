import math
from collections import defaultdict


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)

        def helper(point1, point2):
            x1, y1 = point1[0], point1[1]
            x2, y2 = point2[0], point2[1]
            dy, dx = y2 - y1, x2 - x1
            factor = math.gcd(dy, dx)
            if factor != 0:
                dy = dy // factor
                dx = dx // factor
            if dx < 0:
                dx *= -1
                dy *= -1
            elif dx == 0:
                dy = abs(dy)
            return (dx, dy)

        res = 0
        for firstIdx in range(len(points) - 1):
            slopeMap: dict[tuple[int, int], int] = defaultdict(int)
            for secondIdx in range(firstIdx + 1, len(points)):
                firstPoint, secondPoint = points[firstIdx], points[secondIdx]
                slope = helper(firstPoint, secondPoint)
                slopeMap[slope] += 1
            res = max(res, max(slopeMap.values()) + 1)
        return res
