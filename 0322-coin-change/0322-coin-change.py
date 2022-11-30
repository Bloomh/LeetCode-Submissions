class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        # we will use a list, dp, to keep track of the minimum number of coins needed
        # dp[i] will represent the minimum number of coins needed to sum to i
        # originally, every index from 1 to amount will need to be infinity since we have no way to sum
        dp = defaultdict(lambda: inf)
        
        # for every coin, we will update dp
        for c in coins:
            # we only care if the coin is worth less than our amount, otherwise we can't use it
            if c <= amount:
                # it takes only 1 coin to sum to this coin's value
                dp[c] = 1
                
                # for all values from c+1 to amount (we don't care about smaller or bigger values)
                for i in range(c+1,amount+1):
                    # see if we can sum to i using fewer coins
                    # if dp[i-c] isn't infinity, then we can use our new coin to sum to i
                    # this takes 1 extra coin, so we check if 1 + dp[i-c] is less than dp[i]
                    dp[i] = min(dp[i], 1+dp[i-c])
                    
        # if we never found a valid combination then we return -1
        if dp[amount] == inf:
            return -1
        
        # otherwise just return the min number of coins to sum to amount!
        return dp[amount]