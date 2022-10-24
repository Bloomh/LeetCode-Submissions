class Solution:
    def maxLength(self, arr: List[str]) -> int:
        ans = 0
        sets = []
        for s in arr:
            sSet = set(s)
            if len(sSet) != len(s):
                continue
            n = len(sets)
            for i in range(n):
                arrSet = sets[i]
                if not sSet.intersection(arrSet):
                    newSet = sSet.union(arrSet)
                    sets.append(newSet)
                    ans = max(ans, len(newSet))
            sets.append(sSet)
            ans = max(ans, len(sSet))
        return ans
                