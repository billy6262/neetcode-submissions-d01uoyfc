class Solution:
    def scoreOfString(self, s: str) -> int:
        i = 1
        s = list(s)
        su = 0

        while i < len(s):
            su += abs(ord(s[i -1]) - ord(s[i]))
            i += 1
        return su