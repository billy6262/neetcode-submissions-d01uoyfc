class Solution:
    def maxArea(self, heights: List[int]) -> int:
        H =  heights
        L = 0
        R = len(H) - 1 
        MAX = 0


        while L < R:
            if H[L] >= H[R]:
                MAX = max(MAX, H[R] * (R - L ))
                R -= 1  
            if H[L] < H[R]:
                MAX = max(MAX, H[L] * (R - L ))
                L += 1 

        return MAX 