class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < min_buy:
                min_buy = prices[i]
            else:
                max_profit = max(prices[i] - min_buy, max_profit)
        return max_profit