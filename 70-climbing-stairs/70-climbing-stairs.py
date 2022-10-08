class Solution(object):
    def climbStairs(self, n):
        if n == 1: # only 1 way to go up 1 step
            return 1
        distinct_ways = (1,2) # 1 way to go up 1 step, 2 ways to go up 2 steps
        for i in range(2,n): # go up to n steps
            distinct_ways = (distinct_ways[1], distinct_ways[0] + distinct_ways[1]) # the previous number of ways becomes the second previous number of ways and the previous number of ways becomes the sum of the last two
        return distinct_ways[1] # how many ways to go up n stairs