class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = { 0 : 1}

        presum = 0
        resul = 0

        for num in nums:
            presum += num
            
            diff = presum - k

            if diff in prefix:
                resul += prefix[diff]

            prefix[presum] = 1 + prefix.get(presum, 0)
        return resul