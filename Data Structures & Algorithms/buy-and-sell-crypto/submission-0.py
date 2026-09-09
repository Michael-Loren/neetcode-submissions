class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy, max_profit = 0, 0
        for sell in range(len(prices)):
            if prices[sell] < prices[buy]:
                buy = sell
            max_profit = max(max_profit, prices[sell] - prices[buy])
        

        return max_profit


        