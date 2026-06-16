class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:


        def helper(dirr,row,col):
            if len(self.arr) == len(matrix) * len(matrix[0]):
                return
            self.visited.add((row,col))
            self.arr.append(matrix[row][col])
            if row + dirr[0] >= 0 and row + dirr[0] < len(matrix) and col + dirr[1] >= 0 and col + dirr[1] < len(matrix[0]) and (row + dirr[0],col + dirr[1]) not in self.visited:
                helper(dirr,row + dirr[0],col + dirr[1])
                return
            match dirr:
                case (0,1):
                    helper((1,0),row + 1, col)
                case (1,0):
                    helper((0,-1),row, col - 1)
                case (0,-1):
                    helper((-1,0),row - 1,col)
                case (-1,0):
                    helper((0,1),row,col + 1)
        
        self.visited = set()
        self.arr = []
        helper((0,1),0,0)
        return self.arr