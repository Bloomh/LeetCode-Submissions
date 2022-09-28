class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] > 0: #if the previous sum is positive
                nums[i] += nums[i-1] #add it to this element
            ans = max(ans,nums[i]) #maxmimize answer
        return ans 
            