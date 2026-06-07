class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        n = len(grid)
        queue = collections.deque([(0, 0, 1)])
        visited = {(0, 0)}
        adj = [(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,-1),(-1,0),(-1,1)]

        while queue:
            row, col, dist = queue.popleft()

            if row == n - 1 and col == n - 1:
                return dist

            for r, c in adj:
                nr, nc = row + r, col + c
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist + 1))

        return -1