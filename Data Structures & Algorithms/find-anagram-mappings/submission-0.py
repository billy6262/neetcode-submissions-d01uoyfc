class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nummap =  dict()

        for i,num in enumerate(nums2):
            nummap[num] = i

        arr = []
        for num in nums1:
            arr.append(nummap[num])

        return arr