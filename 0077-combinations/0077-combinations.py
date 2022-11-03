class Solution:
    @lru_cache
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 1:
            return [[i] for i in range(1,n+1)]
        ans = []
        for i in range(1,n):
            ans.extend([combo + [i+1] for combo in self.combine(i,k-1)])
        return ans