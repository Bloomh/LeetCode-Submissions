class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        sums = list(accumulate(nums))
        minDiff = sums[-1]
        ans = 0
        
        for i in range(n):
            left = sums[i]//(i+1)
            right = (sums[-1]-sums[i])//max(1,(n-i-1))
            absDiff = abs(left - right)
            if absDiff < minDiff:
                minDiff = absDiff
                ans = i
        return ans