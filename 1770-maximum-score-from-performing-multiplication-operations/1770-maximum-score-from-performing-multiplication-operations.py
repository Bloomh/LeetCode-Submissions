class Solution:
    def maximumScore(self, nums: List[int], m: List[int]) -> int:
        k = len(m)
        @lru_cache(None)
        def dfs(i, j, k):
            if k == len(m):
                return 0
            return max(nums[i] * m[k] + dfs(i + 1, j, k + 1), nums[j] * m[k] + dfs(i, j - 1, k + 1))
			
        res = dfs(0, len(nums) - 1, 0) 
        dfs.cache_clear()
        return res