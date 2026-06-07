class Solution:
    def solve(self, board: List[List[str]]) -> None:
        all_visited = set()
        def capture(visited, row, col) -> bool:
            # return True if this region touches the border
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
                return True

            if board[row][col] == "X" or (row, col) in visited:
                return False

            visited.add((row, col))
            all_visited.add((row, col))

            touches_border = False
            for r, c in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if capture(visited, row + r, col + c):
                    touches_border = True

            return touches_border

        for rowi in range(len(board)):
            for coli in range(len(board[rowi])):
                if board[rowi][coli] == "O" and (rowi, coli) not in all_visited:
                    region = set()
                    if not capture(region, rowi, coli):
                        for r, c in region:
                            board[r][c] = "X"