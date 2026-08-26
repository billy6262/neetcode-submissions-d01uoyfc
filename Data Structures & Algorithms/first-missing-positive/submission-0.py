class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Pass 1: Replace invalid numbers with a sentinel (n+1)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1
        
        # Pass 2: Mark presence by negating at appropriate indices
        for i in range(n):
            num = abs(nums[i])  # Use abs() in case already marked
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])  # Mark as negative
        
        # Pass 3: Find first positive (unmarked) position
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        
        return n + 1