class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [[-1 for _ in range(m)] for _ in range(n)]

        def edit_distance(i, j):
            if j < 0:
                return i + 1
            if i < 0:
                return j + 1
            if dp[i][j] != -1:
                return dp[i][j]
            if word1[i] == word2[j]:  
                dp[i][j] = edit_distance(i - 1, j - 1) 
            else:
                delete = 1 + edit_distance(i - 1, j)
                insert = 1 + edit_distance(i, j - 1)
                replace = 1 + edit_distance(i - 1, j - 1)
                dp[i][j] = min(delete, insert, replace)

            return dp[i][j]

        return edit_distance(n - 1, m - 1)

# Example usage:
solution = Solution()
result = solution.minDistance("horse", "ros")
print(result)  # Outputs the minimum edit distance
