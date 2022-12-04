class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        buy = prices[0]
        
        for i in range(1, len(prices)):
            ans += max(0, prices[i] - buy)
            buy = prices[i]
        
        return ans