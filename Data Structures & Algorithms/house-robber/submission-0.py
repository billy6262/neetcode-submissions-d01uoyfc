class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = {}

        def helper(i):

            if i > len(nums) - 1:
                return 0

            if i in mem:
                return mem[i]

            temp = max(nums[i] + helper(i + 2), helper(i + 1))
            mem[i] = temp

            return temp
        
        return helper(0)