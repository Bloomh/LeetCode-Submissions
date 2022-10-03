class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0 #answer
        for i in range(1,len(colors)): #go through all the colors except the first
            if colors[i-1] == colors[i]: #if the color we are looking at equals the one before it
                if neededTime[i] >= neededTime[i-1]:
                    ans += neededTime[i-1] #remove the balloon that takes less time
                else:
                    ans += neededTime[i] #remove the balloon that takes less time
                    neededTime[i] = neededTime[i-1] #we already removed the i balloon but we may want to remove the i-1 balloon, so move it to the i spot to access later
        return ans