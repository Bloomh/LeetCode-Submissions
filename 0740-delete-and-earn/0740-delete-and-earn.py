class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        c = defaultdict(int)
        s = set()
        m = -inf
        for num in nums:
            s.add(num)
            c[num] += 1
            m = max(num, m)
        
        dp = [0]*(m+2)
        
        for val in range(1,m+1):
            dp[val+1] = max(dp[val], dp[val-1] + val*c[val])

        return dp[-1]
        