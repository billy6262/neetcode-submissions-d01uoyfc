class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numdic = dict() 

        for i, num in enumerate(nums):
            rem = target - num
            if rem == num:
                continue
            if rem in numdic:
                return [numdic[rem]+ 1 , i + 1]
            
            numdic[num] = i
