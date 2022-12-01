class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        c = defaultdict(int)
        m = -inf
        
        for num in nums:
            c[num] += 1
            m = max(num, m)
        
        dp = [0,c[1]]
        
        for val in range(2,m+1):
            dp.append(max(dp[val-1], dp[val-2] + val*c[val]))

        return dp[-1]
        