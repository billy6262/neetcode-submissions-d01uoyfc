class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numdic = dict() 

        for i, num in enumerate(nums):
            rem = target - num
            if rem == num:
                continue
            if rem in numdic:
                return [min(i ,numdic[rem])+ 1 , max(i ,numdic[rem]) + 1]
            
            numdic[num] = i
