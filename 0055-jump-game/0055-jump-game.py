class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        furthest = 0
        
        for i in range(n):
            if i <= furthest:
                furthest = max(furthest, nums[i] + i)
                if furthest >= n - 1:
                    return True
            else:
                return False