class Solution:
    def DFS(self, r : int, c : int, grid : List[List[int]]):
            if min(r,c) < 0 or r == len(grid) or c == len(grid[0]) or grid[r][c] == "0":
                return
            else:
                grid[r][c] = '0'

            self.DFS(1 + r, c, grid)
            self.DFS(r - 1, c, grid)
            self.DFS(r, 1 + c, grid)
            self.DFS(r, c - 1, grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        iscount = 0

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1":
                    self.DFS(row,col,grid)
                    iscount += 1
        
        return iscount