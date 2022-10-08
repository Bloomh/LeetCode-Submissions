class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = []
        for i in range(m):
            dp.append([]) # add a new row
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i].append(1) # base case – 1 possibility
                else:
                    dp[i].append(dp[i-1][j] + dp[i][j-1]) # recursive relationship
        return dp[-1][-1]