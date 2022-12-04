class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [True] + [False]*(n-1)
        
        for i in range(n):
            if dp[i]:
                s = nums[i]+i
                if s < n - 1:
                    for j in range(i+1,s+1):
                        dp[j] = True
                else:
                    return True
        return False