class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])  #grabing length of the rows an cols

        L = 0
        R = m * n -1

        while L <= R:
            M = (L + R)// 2

            row = M // m
            col = M % m  #this parses the absolute value of the middle point into the grid of the matrix.

            if matrix[row][col] == target:
                return True

            elif matrix[row][col] > target:
                R =  M - 1

            else:
                L = M + 1

        return False