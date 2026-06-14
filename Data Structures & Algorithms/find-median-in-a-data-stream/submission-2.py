
class MedianFinder:

    def __init__(self):
      self.hiheap = []
      self.lowheap = []

    def addNum(self, num: int) -> None:
        if self.hiheap and num > self.hiheap[0]:
            heapq.heappush(self.hiheap,num)
        else:
            heapq.heappush_max(self.lowheap,num)

        if len(self.lowheap) > len(self.hiheap) + 1:
            heapq.heappush(self.hiheap,heapq.heappop_max(self.lowheap))

        if len(self.hiheap) > len(self.lowheap) + 1:
            heapq.heappush_max(self.lowheap,heapq.heappop(self.hiheap))

    def findMedian(self) -> float:
        if len(self.hiheap) > len(self.lowheap):
            return self.hiheap[0]
        elif len(self.lowheap) > len(self.hiheap):
            return self.lowheap[0]
        return (self.lowheap[0] + self.hiheap[0]) / 2.0