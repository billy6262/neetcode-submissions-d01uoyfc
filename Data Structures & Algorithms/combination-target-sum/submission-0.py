class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        allsum = [[]]


        def findsums(current : List[int], m : int):
            if sum(current) == target:
                allsum.append(current)

            elif sum(current) < target:
                for num in nums:
                    if num >= m:
                        findsums(current.copy() + [num], num)

        findsums([], 0)
        allsum.pop(0)

        return allsum