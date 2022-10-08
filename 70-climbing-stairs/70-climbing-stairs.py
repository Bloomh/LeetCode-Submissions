class Solution(object):
    def climbStairs(self, n):
        distinct_ways = [1,2] # 1 way to go up 1 step, 2 ways to go up 2 steps
        for i in range(2,n): # go up to n steps
            distinct_ways.append(distinct_ways[-1] + distinct_ways[-2]) # can come from either of the last two steps
        return distinct_ways[n-1] # how many ways to go up n stairs