class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sm = sum(nums)
        if (sm%2==1):
            return False
        sm//=2
        n = len(nums)
        dp = [False]*(sm+1)
        dp[0] = True
        for num in nums:
            for i in range(sm,0,-1):
                if i>=num:
                    dp[i] = dp[i] or dp[i-num]
        return dp[-1]