class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ksum = sum(arr[:k])
        L = 0
        
        if ksum >= threshold * k:
            sumcount = 1
        else:
            sumcount = 0

        for R in range(k,len(arr)):
            L = R - k
            ksum = ksum + arr[R] - arr[L]
            if ksum >= threshold * k:
                sumcount += 1
        
        return sumcount
