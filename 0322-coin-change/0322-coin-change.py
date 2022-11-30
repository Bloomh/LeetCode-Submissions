class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0]+[inf]*(amount)
        for c in coins:
            if c <= amount:
                dp[c] = 1
                for i in range(c+1,amount+1):
                    dp[i] = min(dp[i], 1+dp[i-c])
        return dp[-1] if dp[-1] != inf else -1