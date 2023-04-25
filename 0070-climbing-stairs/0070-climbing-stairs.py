class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        ways = 0
        # current n is 3, if the last step is 1, then the first step is 2
        one_below_current = 2
        # current n is 3, if the last step is 2, then the firts step is 1
        two_below_current = 1
        for i in range(3, n+1):
            ways = one_below_current + two_below_current
            two_below_current = one_below_current
            one_below_current = ways
        return ways
    
    '''
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        dp = [-1] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
    '''