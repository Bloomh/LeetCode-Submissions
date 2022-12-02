class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        c = defaultdict(int) # this will represent the count of every number – c[num] is the frequency of num in nums
        m = -inf # this is the maximum number in nums
        
        for num in nums: 
            c[num] += 1 # update the frequency of this number
            m = max(num, m) # update our maximum
        
        dp = [0,c[1]] # dp[i] will represent the maximum number of points we can get performing our operation on values from 1 to i (inclusive)
        # we never have the number zero, so dp[0] = 0. dp[1] = c[1] since the number of points we get from deleting 1s is the same as the number of 1s in nums
        
        for val in range(2,m+1): # from 2 to m (inclusive)
            # at any point, we can either delete this number and get val*c[val] points
            # or we can not delete this number and keep the option to delete the previous number (dp[val-1])
            # if we delete this number we cannot delete the previous number, so we use dp[val-2]
            dp.append(max(dp[val-1], dp[val-2] + val*c[val])) 
            # we want to add the maximum of these two options to dp[i]
        # return the max amount of points we can get after going through every possible value
        return dp[m]
        