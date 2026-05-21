class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        currsum = 0

        for num in nums:
            currsum = max(currsum + num, 0)
            maxsum = max(currsum, maxsum)

        if maxsum == 0:
            return max(nums)

        else:
            return maxsum