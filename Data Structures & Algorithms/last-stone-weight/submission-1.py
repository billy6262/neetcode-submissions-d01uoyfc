class Solution:


    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        heapq.heapify_max(stones)
        self.heap = stones

        while len(self.heap) > 1:
            stone1 = heapq.heappop_max(self.heap)
            stone2 = heapq.heappop_max(self.heap)

            newstone = stone1 - stone2

            if newstone > 0:
                heapq.heappush_max(self.heap, newstone)

        return self.heap[0] if self.heap else 0