class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        mx = neededTime[0]
        for i, color in enumerate(colors[1:]):
            if color == colors[i]:
                if neededTime[i+1] >= mx:
                    ans += mx
                    mx = neededTime[i+1]
                else:
                    ans += neededTime[i+1]
            else:
                mx = neededTime[i+1]
        return ans