class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        leftSum = 0
        sumNums = sum(nums)
        minDiff = inf
        ans = 0
        
        for i in range(n):
            leftSum += nums[i]
            leftAvg = leftSum//(i+1)
            rightAvg = (sumNums - leftSum)//max(1,n-i-1)
            
            absDiff = abs(leftAvg - rightAvg)
            if absDiff < minDiff:
                minDiff = absDiff
                ans = i
        
        return ans