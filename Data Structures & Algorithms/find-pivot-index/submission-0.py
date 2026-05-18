class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalr = sum(nums)
        totall = 0

        for ind in range(len(nums)):
            if totall == totalr - nums[ind]:
                return ind

            totall += nums[ind]
            totalr -= nums[ind]

        return -1