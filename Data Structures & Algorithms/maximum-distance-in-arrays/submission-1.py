class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        amin = arrays[0][0]
        amax = arrays[0][-1]
        res = 0

        for i in range(1, len(arrays)):
            nums = arrays[i]
            tmin = nums[0]
            tmax = nums[-1]
            
            res = max(res, abs(tmax - amin), abs(amax - tmin))
            
            amin = min(amin, tmin)
            amax = max(amax, tmax)

        return res