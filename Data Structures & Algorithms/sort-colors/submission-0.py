class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        counts = [0,0,0]
        for num in nums:
            counts[num] += 1

        i = 0
        for col in range(3):
            for x in range(counts[col]):
                nums[i] = col
                i += 1

    