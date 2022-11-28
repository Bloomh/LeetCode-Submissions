class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        curr = None
        ans = []
        for s,e in intervals:
            if not curr:
                curr = [s,e]
            elif s <= curr[1]:
                curr[1] = max(curr[1],e)
            else:
                ans.append(curr)
                curr = [s,e]           
        return ans + [curr]