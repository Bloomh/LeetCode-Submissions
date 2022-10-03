class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        i = 1
        n = len(colors)
        while i < n:
            times = [neededTime[i-1]]
            numToRemove = 0
            while colors[i] == colors[i-1]:
                numToRemove += 1
                heapq.heappush(times, neededTime[i])
                i += 1
                if i == n:
                    break
            if len(times) == 1:
                i += 1
            for j in range(numToRemove):
                ans += heapq.heappop(times)
        return ans