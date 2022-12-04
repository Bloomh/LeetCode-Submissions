class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = list(range(n))
        
        for i in range(n):
            for j in range(i+1, min(n,nums[i]+i+1)):
                dp[j] = min(dp[j],1+dp[i])

        return dp[-1]