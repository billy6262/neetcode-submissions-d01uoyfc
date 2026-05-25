class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return len(nums)
        i = 2
        head = 1

        while i < len(nums):
            if nums[i] == nums[head] == nums[head - 1]:
                nums[i] = None
                i += 1
            else:
                nums[head + 1] = nums[i]
                head += 1
                i += 1

        return head + 1