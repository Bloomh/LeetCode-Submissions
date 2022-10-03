class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        for i, color in enumerate(colors[1:]):
            if color == colors[i]:
                if neededTime[i+1] >= neededTime[i]:
                    ans += neededTime[i]
                else:
                    ans += neededTime[i+1]
                    neededTime[i+1] = neededTime[i]
        return ans