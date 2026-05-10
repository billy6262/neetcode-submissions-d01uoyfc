class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts = {}
        dictt = {}
        if len(t) != len(s):
            return False


        for char in s:
            if char not in dicts:
                dicts[char] = 1
            else:
                dicts[char] += 1

        for char in t:
            if char not in dictt:
                dictt[char] = 1
            else:
                dictt[char] += 1

        for char in t:
            if char not in dicts or dicts[char] != dictt[char]:
                return False

        return True