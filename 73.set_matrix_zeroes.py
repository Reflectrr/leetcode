class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n= len(matrix), len(matrix[0])
        firstRowHasZero, firstColHasZero = False, False

        # check if first row and col have zero
        # because first row and col will be used for storing info about row/col to set zeroes
        for x in range(n):
            if matrix[0][x]==0:
                firstRowHasZero = True
                break
        for y in range(m):
            if matrix[y][0]==0:
                firstColHasZero = True

        # use the corresponding position in the first row/col to tell which row/col to set zeroes
        for y in range(1,m):
            for x in range(1,n):
                if matrix[y][x] == 0:
                    matrix[y][0]=0
                    matrix[0][x]=0

        # use the info store in the first col/row to set zeroes
        for y in range(1,m):
            if matrix[y][0]==0:
                for x in range(1,n):
                    matrix[y][x]=0

        for x in range(1,n):
            if matrix[0][x]==0:
                for y in range(1,m):
                    matrix[y][x]=0

        # update first row and col if needed
        if firstRowHasZero:
            for x in range(n):
                matrix[0][x]=0
        if firstColHasZero:
            for y in range(m):
                matrix[y][0]=0

        return


