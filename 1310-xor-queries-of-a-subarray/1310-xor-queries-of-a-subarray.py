class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pref = [0]
        for num in arr:
            pref.append(pref[-1]^num)
        return [pref[r+1]^pref[l] for (l,r) in queries]