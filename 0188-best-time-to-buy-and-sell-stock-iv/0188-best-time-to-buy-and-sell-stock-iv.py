class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        after = [[0 for _ in range(k+1)] for _ in range(2)]
        curr = [[0 for _ in range(k+1)] for _ in range(2)]

        for i in range(n-1, -1, -1):
            for buy in range(2):
                for t in range(1,k+1):
                    if buy == 1:
                        curr[buy][t] = max(-prices[i] + after[0][t],after[1][t])
                    else:
                        curr[buy][t] = max(prices[i] + after[1][t-1],after[0][t])
            after = curr
        
        return after[1][k]