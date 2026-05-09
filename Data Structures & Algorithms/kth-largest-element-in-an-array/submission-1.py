class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums.append(nums[0])

        cur = len(nums) // 2

        while cur > 0:

            i = cur

            while 2 * i < len(nums): #this is the sorting section and it will itterate till the value meets the heap citeria
                lind = i * 2
                rind = i * 2 + 1
                if len(nums) > rind and nums[rind] > nums[lind] and  nums[rind] > nums[i]:
                    temp = nums[i]
                    nums[i] = nums[rind]
                    nums[rind] = temp
                    i = rind
                elif nums[lind] > nums[i]:
                    temp = nums[i]
                    nums[i] = nums[lind]
                    nums[lind] = temp
                    i = lind
                else:
                    break
            cur -= 1 
        
        c = 1

        while c < k:
            i = 1
            nums[1] = nums.pop()
            while 2 * i < len(nums): #this is the sorting section and it will itterate till the value meets the heap citeria
                lind = i * 2
                rind = i * 2 + 1
                if len(nums) > rind and nums[rind] > nums[lind] and  nums[rind] > nums[i]:
                    temp = nums[i]
                    nums[i] = nums[rind]
                    nums[rind] = temp
                    i = rind
                elif nums[lind] > nums[i]:
                    temp = nums[i]
                    nums[i] = nums[lind]
                    nums[lind] = temp
                    i = lind
                else:
                    break
            c += 1
        return nums[1]

