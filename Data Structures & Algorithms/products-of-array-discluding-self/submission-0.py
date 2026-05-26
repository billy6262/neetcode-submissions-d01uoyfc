class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [1] * len(nums)
        
        # First pass: compute prefix products
        prefix = 1
        for i in range(len(nums)):
            arr[i] = prefix
            prefix *= nums[i]
        
        # Second pass: compute postfix products and multiply
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            arr[i] *= postfix
            postfix *= nums[i]
        
        return arr
