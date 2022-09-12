class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [-1 if i not in coins else 1 for i in range(1,amount+1)]
        for i in range(amount):
            if dp[i]!=-1:
                for c in coins:
                    if i+c<amount:
                        dd = dp[i+c]
                        if dd == -1:
                            dp[i+c]=dp[i]+1
                        else:
                            dp[i+c] = min(dp[i+c],dp[i]+1)
        return dp[-1]
        