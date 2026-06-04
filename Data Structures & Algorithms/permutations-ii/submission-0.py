class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[nums[0]]]

        perms = self.permuteUnique(nums[1:])
        
        res = set()
        for p in perms:
            for i in range(len(p) + 1):
                t = p.copy()
                t.insert(i, nums[0])
                res.add(tuple(t))

        return [list(p) for p in res]