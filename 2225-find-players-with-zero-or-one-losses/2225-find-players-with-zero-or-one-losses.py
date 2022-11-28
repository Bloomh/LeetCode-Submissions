class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dct = defaultdict(int)
        for w,l in matches:
            dct[w] = dct[w]
            dct[l] += 1
        ans = [[],[]]
        for key,val in sorted(dct.items()):
            if val < 2:
                ans[val].append(key)
        return ans