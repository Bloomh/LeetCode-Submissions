class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # here the 0th index is the second to last step and the 1st index is the last step
        min_costs = (cost[0], cost[1]) # start with the starting steps
        
        for i in range(2, len(cost)): # from index 2 until the end of the staircase
            min_costs = (min_costs[1], cost[i] + min(min_costs[0], min_costs[1])) # the last step becomes the second to last step, the new last step uses our recursive relationship
        
        return  min(min_costs) # since we can reach the end from either of the last two steps, we return the minimum from either step
            
        