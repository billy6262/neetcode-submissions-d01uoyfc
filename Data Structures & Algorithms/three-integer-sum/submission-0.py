class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = []
        nums.sort()

        for i, base in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            L = i + 1
            R = len(nums) - 1
            while L < R:
                total = nums[L] + nums[R] + base
                if total > 0:
                    R -= 1
                elif total < 0:
                    L += 1
                else:
                    arr.append([base, nums[L], nums[R]])
                    while L < R and nums[L] == nums[L+1]:
                        L += 1
                    while L < R and nums[R] == nums[R-1]:
                        R -= 1
                    L += 1
                    R -= 1
        return arr