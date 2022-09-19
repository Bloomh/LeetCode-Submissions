class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target+1)] 
        for c in candidates:                                  
            for i in range(c, target+1):                     
                if i == c: 
                    dp[i].append([c]) #add it if it is itself
                for comb in dp[i-c]: #for each combo that can sum up to here
                    dp[i].append(comb + [c]) # add combo w new element
        return dp[-1]
                