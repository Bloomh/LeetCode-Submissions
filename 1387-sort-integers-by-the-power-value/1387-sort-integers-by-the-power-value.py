class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @lru_cache(None)
        def power(x):
            return 1 if x ==1 else 1 + power(3*x+1) if x % 2 else 1 + power(x//2)
        return heapq.nsmallest(k, range(lo,hi+1), key = power)[-1]