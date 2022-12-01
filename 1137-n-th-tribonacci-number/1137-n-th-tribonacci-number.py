class Solution:
    def tribonacci(self, n: int) -> int:
        tribonnaci_nums = [0,1,1] # the first three tribonnaci numbers are 0, 1, and 1
        for i in range(3, n+1):
            tribonnaci_nums.append(tribonnaci_nums[-1] + tribonnaci_nums[-2] + tribonnaci_nums[-3])
        return tribonnaci_nums[n]