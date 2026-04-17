class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = l + (r - l) // 2  # Prevents overflow
            
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1  # Target is in right half
            else:
                r = m - 1  # Target is in left half
        
        return -1