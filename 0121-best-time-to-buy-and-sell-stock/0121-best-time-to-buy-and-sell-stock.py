class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        buy = float("inf")
        profit = 0
        for i in prices:
            if i < buy:
                buy = i
            else:
                profit = max(profit, i - buy)
        '''
        buy = float("-inf")
        profit = 0
        for i in prices:
            buy = max(-i, buy)
            profit = max(profit, buy + i)
        return profit
        
        