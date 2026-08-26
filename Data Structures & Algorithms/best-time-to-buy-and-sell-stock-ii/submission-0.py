class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        total = 0

        for i in range(1, len(prices)):  # Start from index 1
            if prices[i - 1] < prices[i]:
                total += prices[i] - prices[i - 1]

        return total