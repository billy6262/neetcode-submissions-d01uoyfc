class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1dict = dict()
        for i, L in enumerate(s1):
            s1dict[L] = 1 + s1dict.get(L, 0) 

        for L, lchar in enumerate(s2):
            checkset = dict()

            for R in range(L, L + len(s1) ):
                if R >= len(s2):
                    break
                checkset[s2[R]] = 1 + checkset.get(s2[R], 0)

                if checkset[s2[R]] > s1dict.get(s2[R], 0):
                    break
            else:
                return True
        return False

        