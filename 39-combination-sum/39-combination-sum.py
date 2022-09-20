class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target+1)] 
        for c in candidates:
            if c>target:
                continue
            dp[c].append([c])
            for i in range(c+1, target+1):                     
                for comb in dp[i-c]: #for each combo that can sum up to here
                    dp[i].append(comb + [c]) # add combo w new element
        return dp[-1]