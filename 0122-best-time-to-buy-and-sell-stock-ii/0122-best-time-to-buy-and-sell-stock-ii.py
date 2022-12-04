class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        buy = inf
        
        for price in prices:
            ans += max(0, price - buy)
            buy = price
        
        return ans