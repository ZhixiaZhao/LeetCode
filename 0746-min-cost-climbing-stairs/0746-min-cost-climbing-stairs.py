class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        dp0 = cost[0]
        dp1 = cost[1]
        for i in range(2, length):
            cost_min = cost[i] + min(dp0, dp1)
            dp0 = dp1
            dp1 = cost_min
        return min(dp0, dp1)
        
        