class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        counts = {}
        heap = []

        for num in nums:
            counts[num] = counts.get(num,0) + 1

        for num,count in counts.items():
            heapq.heappush(heap,(count,num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

        