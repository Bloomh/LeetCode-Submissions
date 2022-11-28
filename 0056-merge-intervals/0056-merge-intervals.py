class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        curr = intervals[0]
        ans = []
        for s,e in intervals:
            if s <= curr[1]:
                curr[1] = max(curr[1],e)
            else:
                ans.append(curr)
                curr = [s,e]           
        return ans + [curr]