class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        remain = {}
        for num in range(len(nums)):
            rem = target - nums[num]

            if rem in remain:
                return [remain[rem],num]

            else:
                remain[nums[num]] = num