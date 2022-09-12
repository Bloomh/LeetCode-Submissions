class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        people = sorted([[speed[i],efficiency[i]] for i in range(n)],key=lambda x:-x[1])
        worstSpeeds = []
        worstEff = float('inf')
        currSum = 0
        ans = 0
        for i in range(k):
            currSum += people[i][0]
            heapq.heappush(worstSpeeds,people[i][0])
            worstEff = people[i][1]
            ans = max(ans,(currSum*worstEff))
        for i in range(k,n):
            worstEff = people[i][1]
            currSum+=people[i][0]-heapq.heappushpop(worstSpeeds,people[i][0])
            ans = max(ans,(currSum*worstEff))
        return ans%(10**9+7)