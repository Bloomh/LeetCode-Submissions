class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        # store the length of our array
        n = len(nums)
        
        # this will keep track of the sum from the left up to the index we are looknig at
        leftSum = 0
        
        # the sum from the right begins with the full array
        rightSum = sum(nums)
        
        # we will store the minimum absolute difference we find so we can compare
        minDiff = inf
        
        # we will start with 0 as our answer
        ans = 0
        
        for i in range(n):
            # we add nums[i] to the left sum and subtract it from the right sum since now we are looking at index i
            leftSum += nums[i]
            rightSum -= nums[i]
            
            # the left average is the leftsum divided by the number of elements (i+1)
            leftAvg = leftSum//(i+1)
            
            # the right average is the rightsum divided by the number of elements (n-i-1)
            # it is possible that this will be zero so we avoid that by using max(1,n-i-1)
            rightAvg = rightSum//max(1,n-i-1)
            
            # now we calculate the absolute difference between the averages
            absDiff = abs(leftAvg - rightAvg)
            
            # if this is smaller than the minimum difference we have seen so far then we need to update our answer!
            if absDiff < minDiff:
                minDiff = absDiff
                ans = i
        
        return ans