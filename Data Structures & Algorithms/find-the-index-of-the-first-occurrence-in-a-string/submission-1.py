class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        slen = len(needle) 

        for i in range(len(haystack)):
            if i + slen <= len(haystack) and haystack[i: i + slen] == needle:
                return i
        return -1

                
            

        