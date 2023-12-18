class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp_i_0 = 0
        dp_i_1 = float("-inf")
        for i in prices:
            dp_i_0 = max(dp_i_0, dp_i_1 + i)
            dp_i_1 = max(dp_i_1, dp_i_0 - i)
        return dp_i_0