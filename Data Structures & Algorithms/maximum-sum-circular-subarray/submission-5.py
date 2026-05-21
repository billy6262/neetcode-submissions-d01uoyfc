class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxsum = nums[0]
        maxnegsum = nums[0]
        cursum = 0
        curnegsum = 0
        total = 0

        for num in nums:
            total += num

            cursum = max(cursum + num, num)
            curnegsum = min(curnegsum + num, num)


            maxnegsum = min(maxnegsum, curnegsum)
            maxsum = max(cursum, maxsum)

        if maxsum < 0:
            return maxsum

        return max(maxsum, total - maxnegsum)
