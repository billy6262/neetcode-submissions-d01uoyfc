class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr = [[]]

        for num in nums:
            newsubsets = []
            for sub in arr:
                newsubsets.append(sub + [num])
            arr.extend(newsubsets)
        
        return arr