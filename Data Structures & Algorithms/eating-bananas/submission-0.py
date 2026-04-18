class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles) #this sets the upper bound 

        while low <= high:
            mid = (low + high) // 2

            tt = sum(math.ceil(p / mid) for p in piles) #inline for each loop summing the time it takes to consume each pile

            if tt <= h:
                high = mid - 1

            else:
                low = mid + 1
        return low