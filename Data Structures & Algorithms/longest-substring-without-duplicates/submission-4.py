class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mlen = 0
        L = 0
        lset = set()


        for R in range(len(s)):
            while s[R] in lset:
                lset.remove(s[L])
                L += 1

            lset.add(s[R])
            mlen = max(mlen, R - L + 1)

        return mlen




        