class Solution:
    def tribonacci(self, n: int) -> int:
        tribonnaci_nums = (0,1,1) # the first three tribonnaci numbers are 0, 1, and 1
        while n > 2:
            tribonnaci_nums = (tribonnaci_nums[-2], tribonnaci_nums[-1] , tribonnaci_nums[-1] + tribonnaci_nums[-2] + tribonnaci_nums[-3]) # the next tribonnaci number is the sum of the last three!
            n -= 1
        return tribonnaci_nums[n] # return the nth tribonnaci number