class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        dp = [nums[0]] #keep track of the best sum up to each index
        for i in range(1,len(nums)):
            if dp[-1] < 0: #if the previous max subarray is negative
                dp.append(nums[i]) # we start our subarray sum fresh with just nums[i]
            else: #if the previous sum was positive, we want to add it
                dp.append(nums[i] + dp[-1])
            maxSum = max(maxSum,dp[-1])
        return maxSum
            