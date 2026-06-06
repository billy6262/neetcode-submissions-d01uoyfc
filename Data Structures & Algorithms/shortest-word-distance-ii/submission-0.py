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

        for i1 in word1i:
            for i2 in word2i:
                mindist = min(max(i1,i2)-min(i1,i2), mindist)

        return mindist


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
