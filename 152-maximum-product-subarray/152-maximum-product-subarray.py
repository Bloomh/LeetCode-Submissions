class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        n = len(nums)
        up = [0]+nums
        down = [0]*(n+1)
        for i in range(n):
            up[i+1] = max(nums[i],up[i]*nums[i],down[i]*nums[i],0)
            down[i+1] = min(nums[i],up[i]*nums[i],down[i]*nums[i],0)
        return max(up)