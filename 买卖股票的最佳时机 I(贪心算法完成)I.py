"""贪心算法"""
class Solution:
    def maxProfit(self, prices:list):
        max = 0 
        for i in range(len(prices)-1):
            if prices[i]<prices[i+1]:
                max = prices[i+1]-prices[i]
        
        return max
