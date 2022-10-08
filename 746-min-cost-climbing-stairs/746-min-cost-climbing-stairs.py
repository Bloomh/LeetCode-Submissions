class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        min_costs = [cost[0], cost[1]] # start with the starting steps
        
        for i in range(2, len(cost)): # from index 2 until the end of the staircase
            min_costs.append(cost[i] + min(min_costs[i-1], min_costs[i-2]))
        
        return  min(min_costs[-1], min_costs[-2]) # since we can reach the end from either of the last two steps, we return the minimum from either step
            
        