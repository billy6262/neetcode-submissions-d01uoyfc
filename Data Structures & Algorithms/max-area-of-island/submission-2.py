class Solution:
    def DFScount(self, r, c, grid) -> int:
        if min(r,c) < 0 or r == len(grid) or c == len(grid[0]) or grid[r][c] == 0:
            return 0
        else:
            grid[r][c] = 0

            lcount = 1

            lcount += self.DFScount( r + 1, c, grid)
            lcount += self.DFScount(r - 1, c, grid)
            lcount += self.DFScount(r, c + 1, grid)
            lcount += self.DFScount(r, c - 1, grid)

            return lcount


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxland = 0

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if  grid[row][col] == 1:
                    maxland = max(maxland, self.DFScount(row, col, grid))
        
        return maxland
