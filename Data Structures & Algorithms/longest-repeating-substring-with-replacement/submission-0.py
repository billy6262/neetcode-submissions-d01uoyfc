class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lettercount = {}
        L = 0
        maxlen = 0

        for R in range(len(s)):
            lettercount[s[R]] = 1 + lettercount.get(s[R], 0)

            while lettercount and R - L + 1 - max(lettercount.values()) > k:
                lettercount[s[L]] -= 1
                L += 1

            maxlen = max(maxlen, R - L + 1)

        return maxlen