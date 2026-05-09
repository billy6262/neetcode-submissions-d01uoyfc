class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

        heapq.heapify_max(nums)

        i = 1
        while i < k:
            heapq.heappop_max(nums)
            i += 1

        return heapq.heappop_max(nums)