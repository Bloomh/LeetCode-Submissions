class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[int(i<k) for i in range(target)]] + [[0]*target for _ in range(n-1)]
        for i in range(1,n):
            for j in range(min(k*(i+1),target)):
                dp[i][j] += sum(dp[i-1][max(0,j-k):j])
        return dp[-1][-1]%(10**9+7)