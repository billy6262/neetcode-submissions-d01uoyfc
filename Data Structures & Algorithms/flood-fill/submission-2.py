class Solution:
    def DFS(self, r : int, c : int, ncol : int, ocol : int, grid : List[List[int]]):
            if min(r,c) < 0 or r == len(grid) or c == len(grid[0]) or grid[r][c] != ocol:
                return
            else:
                grid[r][c] = ncol

            self.DFS(1 + r, c, ncol, ocol, grid)
            self.DFS(r - 1, c, ncol, ocol, grid)
            self.DFS(r, 1 + c, ncol, ocol, grid)
            self.DFS(r, c - 1, ncol, ocol, grid)
        

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        oldcolor = image[sr][sc]
        if oldcolor == color:
            return image
        self.DFS(sr,sc,color,oldcolor,image)

        return image
        
