from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
      self.nums = SortedList()  

    def addNum(self, num: int) -> None:
        self.nums.add(num)

    def findMedian(self) -> float:
        if len(self.nums) == 1:
            return self.nums[0]
        if len(self.nums) % 2 == 0:
            return (self.nums[(len(self.nums)- 1)//2] + self.nums[(len(self.nums)//2)]) / 2
        else:
            return self.nums[len(self.nums)//2]
        