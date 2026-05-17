class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minval = prices[0]
        profit = 0


        for val in prices:
            if val > minval and val - minval > profit:
                profit = val - minval

            if val < minval:
                minval = val

        return profit
        