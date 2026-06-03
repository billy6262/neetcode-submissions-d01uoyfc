class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict() #keyed off the value of the dict containing all letters in a word

        for word in strs:
            key = "".join(sorted(word))
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]

        arr = []
        for group in groups.values():
            arr.append(group)

        return arr