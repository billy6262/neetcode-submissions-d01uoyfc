class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        visited = set()
        paterns = []
        def BFS(row,col):
            if grid[row][col] == 0 or (row, col) in visited:
                return
            cords = [(1,0),(-1,0),(0,1),(0,-1)]
            que = [(row,col)]
            pat = set()
            visited.add((row, col))

            while que:
                cur = que.pop(0)
                pat.add((cur[0] - row, cur[1] - col))
                for r,c in cords:
                    nr, nc = cur[0] + r, cur[1] + c
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        que.append((nr, nc))
            if pat and pat not in paterns:
                paterns.append(pat)

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                BFS(row,col)

        return len(paterns)