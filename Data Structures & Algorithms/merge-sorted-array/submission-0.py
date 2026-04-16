class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ind = 0

        L = nums1[0:m]
        R = nums2

        while len(L) > 0 and len(R) > 0:
            if L > R:
                nums1[ind] = R.pop(0)
            else:
                nums1[ind] = L.pop(0)
            ind += 1

        if len(L) > 0:
            for n in L:
                nums1[ind] = n
                ind +=1
        
        if len(R) > 0:
            for n in R:
                nums1[ind] = n
                ind +=1

                 
