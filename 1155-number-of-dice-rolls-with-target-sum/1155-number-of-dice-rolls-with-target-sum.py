class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if target>n*k:
            return 0
        dp = [[int(i<k) for i in range(target)]] + [[0]*target for _ in range(n-1)] #
        for i in range(1,n): #up until n
            for j in range(min(k*(i+1),target)): #go to the end of what can be reached with i dice rolls
                dp[i][j] += sum(dp[i-1][max(0,j-k):j]) #we can reach the sum j from any number between j-k and j-1
        return dp[-1][-1]%(10**9+7) #return the answer mod 10^9+7