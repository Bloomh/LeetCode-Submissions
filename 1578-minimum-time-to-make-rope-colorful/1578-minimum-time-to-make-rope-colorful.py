class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        i = 1
        n = len(colors)
        while i < n:
            maxTime = neededTime[i-1]*(colors[i] == colors[i-1])
            numToRemove = 0
            while colors[i] == colors[i-1]:
                numToRemove += 1
                if neededTime[i] > maxTime:
                    ans += maxTime
                    maxTime = neededTime[i]
                else:
                    ans += neededTime[i]
                i += 1
                if i == n:
                    break
            if maxTime == 0:
                i += 1
        return ans