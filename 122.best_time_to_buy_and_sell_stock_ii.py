class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        totalProfit = 0
        for index in range(len(prices)-1):
            if prices[index] < prices[index+1]:
                totalProfit+=prices[index+1]-prices[index]
        return totalProfit
