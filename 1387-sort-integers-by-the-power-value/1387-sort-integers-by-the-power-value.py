class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @lru_cache(None)
        def power(x):
            if x == 1:
                return 1
            elif x % 2:
                return 1 + power(3*x+1)
            return 1 + power(x//2)
        return heapq.nsmallest(k, range(lo,hi+1), key = power)[-1]