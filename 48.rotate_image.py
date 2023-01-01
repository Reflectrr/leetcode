class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        for y in range(n // 2):
            for x in range(n - 1 - 2 * y):
                temp = matrix[y][x + y]
                matrix[y][x + y] = matrix[n - x - 1 - y][y]
                matrix[n - x - 1 - y][y] = matrix[n - y - 1][n - x - y - 1]
                matrix[n - y - 1][n - x - y - 1] = matrix[x + y][n - y - 1]
                matrix[x + y][n - y - 1] = temp
