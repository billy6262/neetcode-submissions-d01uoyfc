class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [None] * (len(nums) * 2)  # Create a list with 2n elements
        
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i + len(nums)] = nums[i]
        
        return ans