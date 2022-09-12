class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        if n == 2:
            return max(nums)
        dp = nums
        dp[2] = dp[2]+dp[0]
        for i in range(3,n):
            dp[i]+=max(dp[i-2],dp[i-3])
        return max(dp[-1],dp[-2])
        
        