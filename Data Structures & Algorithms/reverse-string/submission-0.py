class Solution:
    def reverseString(self, s: List[str]) -> None:
        L = 0
        R = len(s) - 1
        while L < R:
            tmp = s[L]
            s[L] = s[R]
            s[R] = tmp
            R -= 1
            L += 1
        