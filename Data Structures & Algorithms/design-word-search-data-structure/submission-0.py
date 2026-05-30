class trie:
    def __init__(self):
        self.isword = False
        self.children = dict()

class WordDictionary:

    def __init__(self):
        self.root =  trie()

        

    def addWord(self, word: str) -> None:
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = trie()
            cur = cur.children[letter]
        cur.isword = True
        

    def search(self, word: str) -> bool:
        def DFS(level, cur):
            if level == len(word):
                return cur.isword

            if word[level] == ".":
                for child in cur.children.values():
                    if DFS(level + 1, child):
                        return True
                return False

            else:
                if word[level] not in cur.children:
                    return False
                return DFS(level + 1, cur.children[word[level]])
        return DFS(0,self.root)

        
