class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        for i in range(1,len(colors)): #go through all the balloons except the first
            if colors[i-1] == colors[i]: #if the color we are looking at equals the one before it
                if neededTime[i] >= neededTime[i-1]: #if the previous balloon is easier to remove
                    ans += neededTime[i-1] #remove the previous balloon
                else: #if it is quicker to remove this balloon
                    ans += neededTime[i] #remove it
                    neededTime[i] = neededTime[i-1] #we already removed the balloon at i but we may want to remove the balloon at i-1, so move it to index i to access later
        return ans