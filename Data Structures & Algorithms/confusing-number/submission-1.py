class Solution:
    def confusingNumber(self, n: int) -> bool:
        s = str(n)
        mapping = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        
        rotated = []
        for char in s[::-1]:
            if char not in mapping:
                return False
            rotated.append(mapping[char])
        
        return "".join(rotated) != s