class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        # Create prefix sum matrix with extra row/col (all zeros initially)
        self.sumMat = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        # Fill the prefix sum matrix
        for r in range(ROWS):
            prefix = 0  # Running sum for current row
            for c in range(COLS):
                # Add current element to row prefix
                prefix += matrix[r][c]
                # Get sum from cell above
                above = self.sumMat[r][c + 1]
                # Fill in: current_row_sum + sum_from_above
                self.sumMat[r + 1][c + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Adjust indices to match our prefix matrix (which is 1-indexed)
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        
        # Apply inclusion-exclusion principle
        bottomRight = self.sumMat[row2][col2]      # Sum from (0,0) to (row2, col2)
        above = self.sumMat[row1 - 1][col2]        # Sum from (0,0) to (row1-1, col2)
        left = self.sumMat[row2][col1 - 1]         # Sum from (0,0) to (row2, col1-1)
        topLeft = self.sumMat[row1 - 1][col1 - 1]  # Sum from (0,0) to (row1-1, col1-1)
        
        return bottomRight - above - left + topLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)