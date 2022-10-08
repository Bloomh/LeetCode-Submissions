class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        @cache
        def minCost(i): # determine the min cost to reach step i
            if i <= 1: # if it is a starting step
                return cost[i] # just return the price
            return cost[i] + min(minCost(i-1), minCost(i-2)) # recursive relationship
        
        n = len(cost)
        return min(minCost(n-1), minCost(n-2)) # since we can reach the end from either of the last two steps, we return the minimum from either step
            
        