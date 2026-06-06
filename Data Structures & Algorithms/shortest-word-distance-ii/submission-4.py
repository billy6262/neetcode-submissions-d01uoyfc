class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordmap = dict()

        for i, word in enumerate(wordsDict):
            t  = self.wordmap.get(word,[])
            t.append(i)
            self.wordmap[word] = t

    def shortest(self, word1: str, word2: str) -> int:
        mindist = float("inf")

        word1i = self.wordmap[word1]
        word2i = self.wordmap[word2]
        i = 0
        j = 0

        while i < len(word1i) and j < len(word2i):
            mindist = min(mindist, abs(word1i[i] - word2i[j]))

            if word1i[i] < word2i[j]:
                i += 1
            else:
                j += 1
               
        return mindist


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
