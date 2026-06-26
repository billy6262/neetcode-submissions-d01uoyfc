class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        numslen = len(nums)
        nums.sort()
        quad = set()


        for il in range(numslen):
            numl = nums[il]
            for ill in range(il + 1,numslen):
                numll = nums[ill]
                left = ill + 1
                right = numslen - 1
                base = numl + numll

                while left < right:
                    if base + nums[left] + nums[right] > target:
                        right -= 1
                    elif base + nums[left] + nums[right] < target:
                        left += 1
                    else:

                        quad.add((numl,numll,nums[left],nums[right]))
                        left += 1

        return list(quad)