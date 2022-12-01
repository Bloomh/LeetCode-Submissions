class Solution:
    @cache
    def tribonacci(self, n: int) -> int:
        if n == 0: # the 0th tribonacci number is 0
            return 0
        if n <= 2: # the 1st and 2nd tribonacci numbers are 1
            return 1
        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3) # the nth tribonacci number is the sum of the n-1th, n-2th, and n-3th tribonacci numbers