class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        mostRecent = {}
        ans = 0
        for task in tasks:
            if task in mostRecent:
                ans += max(0, space - (ans - mostRecent[task]))
            ans += 1
            mostRecent[task] = ans
        return ans