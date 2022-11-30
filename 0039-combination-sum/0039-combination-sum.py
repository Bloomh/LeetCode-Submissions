class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target+1)]
        
        for c in candidates:
            if c <= target:
                dp[c] += [[c]]
                for i in range(c+1,target+1):
                    for combo in dp[i-c]:
                        dp[i] += [combo + [c]]

        return dp[-1]