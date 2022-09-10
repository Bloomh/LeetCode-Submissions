class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k >= len(prices) / 2: 
            profit = 0;
            for i in range(1,len(prices)):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit
        buy = [float('-inf')]*(k+1) #set up k times you will buy (0 is extra space)
        sell = [0]*(k+1) #sell k times
        for price in prices:
            for i in range(1,k+1):
                buy[i] = max(buy[i],sell[i-1]-price) #get the best possible purchase on day 1 (either stick with what is there or sell yesterday and buy today)
                sell[i] = max(sell[i],buy[i]+price) #how much money you have in liquid assets and from selling your stock (either same as last transaction or more if you sell today and it increases your total)
        return sell[k]