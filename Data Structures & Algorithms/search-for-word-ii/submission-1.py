class trie():
    def __init__(self):
        self.word = False
        self.children = {}





class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = trie()

        for word in words:
            cur = root
            for char in word:
                if char not in cur.children:
                    cur.children[char] = trie()
                cur = cur.children[char]
            cur.word = True

        result = []
        visited = set()

        def trav(curr, col , row, word):
            dirc = [(0,1),(0,-1),(1,0),(-1,0)]

            if row >= 0 and col >= 0 and row < len(board) and col < len(board[0]) and (row,col) not in visited and board[row][col] in curr.children:
                curr = curr.children[board[row][col]]
                visited.add((row,col))
                word += board[row][col]
            else:
                return 

            if curr.word:
                result.append(word)
                curr.word = False

            for d in dirc:
                trav(curr, col + d[0], row + d[1], word)

            visited.remove((row,col))

        for row in range(len(board)):
            for col in range(len(board[row])):
                trav(root,col,row, "")


        return result


