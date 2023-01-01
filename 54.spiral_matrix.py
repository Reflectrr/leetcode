import math

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        m, n = len(matrix), len(matrix[0])
        for level in range(math.ceil(min(m, n) / 2)):
            levelm, leveln = m - 2 * level, n - 2 * level
            for index in range(leveln - 1):
                res.append(matrix[level][index + level])
            for index in range(levelm):
                res.append(matrix[index + level][n - 1 - level])
            if level != m - 1 - level and level != n-1-level:
                for index in range(leveln-2, 0, -1):
                    res.append(matrix[m - 1 - level][index + level])
                for index in range(levelm-1, 0, -1):
                    res.append(matrix[index + level][level])
        return res
