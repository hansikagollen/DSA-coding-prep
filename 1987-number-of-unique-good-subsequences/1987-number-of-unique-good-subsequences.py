class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        mod = 10**9 + 7
        dp = [[0, 0] for _ in range(2)]
        n = len(binary)
        
        for ch in binary:
            if ch == '0':
                dp[0][0] = 1
                dp[1][0] = (dp[1][0] + dp[1][1]) % mod
            else:
                dp[1][1] = (dp[1][0] + dp[1][1] + 1) % mod
        result = (dp[0][0] + dp[0][1] + dp[1][0] + dp[1][1]) % mod
        return result


sol = Solution()

print(sol.numberOfUniqueGoodSubsequences("001"))  
print(sol.numberOfUniqueGoodSubsequences("11"))   
print(sol.numberOfUniqueGoodSubsequences("101"))  