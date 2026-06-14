class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numdict = defaultdict(int)

        for num in nums:
            numdict[num] += 1

        return max(numdict.items(), key=lambda x: x[1])[0]