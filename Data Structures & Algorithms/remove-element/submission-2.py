class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        emptyInd = None
        ind = 0
        x = 0 
        

        while ind < len(nums):
            if nums[ind] == val:
                nums[ind] = None
                if emptyInd == None:
                    emptyInd = ind
            else:
                x += 1
                if emptyInd != None:
                    nums[emptyInd] = nums[ind]
                    nums[ind] = None
                    emptyInd += 1
            ind += 1
        return x