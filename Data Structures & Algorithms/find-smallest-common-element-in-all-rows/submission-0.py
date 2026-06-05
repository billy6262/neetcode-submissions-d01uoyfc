class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        nums = dict()
        
        I = 0

        while I < len(mat[0]):
            for row in mat:
                count = nums.get(row[I], 0) + 1
                nums[row[I]] = count
                if count == len(mat):
                    return row[I]
            I += 1
        return -1