class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # dp[i] will keep track of all the ways to sum to i using values in candidates
        # originally it is all empty lists since we don't know if/how we can sum to anything
        dp = [[] for _ in range(target+1)]
        
        # we will go through all the different candidates and use them to add to dp
        for c in candidates:
            # if c > target then there is no way we can sum to target using it, so we need c <= target
            if c <= target:
                # we can sum to c with just the value c
                dp[c].append([c])
                # for all values bigger than c, we need to use previous entries in dp to see if we can sum
                for i in range(c+1,target+1):
                    # for all the ways we can sum to i-c, we can add c and sum to i
                    for combo in dp[i-c]:
                        # the way to sum to i is to add c to our previous combination which summed to i-c
                        dp[i].append(combo + [c])
                        
        # return all the unique ways to sum to target!
        return dp[target]