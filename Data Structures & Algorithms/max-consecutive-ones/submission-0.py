class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        count = 0

        for num in nums:
            if num == 1:
                count = count + 1
            elif num == 0:
                count = 0
            if count > max:
                max = count
        return max
        