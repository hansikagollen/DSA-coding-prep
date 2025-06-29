class Solution:
    def climbStairs(self, n: int) -> int:
        # Edge cases
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Dynamic programming array
        dp = [0] * (n + 1)  # Considering zero steps we need n+1 places
        dp[1] = 1
        dp[2] = 2
        
        # Fill the dp array
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
