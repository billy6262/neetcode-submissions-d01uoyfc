class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = set()
        fresh = set()
        card = [(0,1),(0,-1),(1,0),(-1,0)]
        def can_rot(r,c):
            for dr,dc in card:
                nr, nc = r + dr, c + dc
                if len(grid) > nr >= 0 and len(grid[0]) > nc >= 0:
                    if (nr, nc) in rotten:
                        return True
            return False

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fresh.add((row,col))
                if grid[row][col] == 2:
                    rotten.add((row,col))

        if not fresh: return 0
        time = 0

        while True:
            to_rot = set()
            for r, c in fresh:
                if can_rot(r, c):
                    to_rot.add((r, c))
            
            if not to_rot:
                break
            
            fresh -= to_rot
            rotten |= to_rot
            time += 1
        
        if fresh:
            return -1
        return time