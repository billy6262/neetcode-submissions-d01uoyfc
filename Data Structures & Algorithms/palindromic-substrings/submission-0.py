class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        def countpal(s,L,R):
            count = 0
            if L < 0 or R > len(s) - 1:
                return 0

            while s[L] == s[R]:
                count += 1
                if L == 0 or R == len(s) - 1:
                    return count
                L -= 1
                R += 1
            return count

        res = 0
        for i in range(len(s)):
            res += countpal(s,i,i)
            res += countpal(s,i,i+1)

        return res
                
                    