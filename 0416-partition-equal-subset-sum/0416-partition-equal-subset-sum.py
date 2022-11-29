class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        dp = [True] + [False]*(s//2)
        for num in nums:
            for i in range(s//2-num,-1,-1):
                if dp[i]:
                    dp[i+num] = True
        return dp[-1]