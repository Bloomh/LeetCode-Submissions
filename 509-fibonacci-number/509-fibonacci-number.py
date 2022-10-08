class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        prev_nums = (0,1)
        for i in range(2,n+1):
            prev_nums = (prev_nums[1], prev_nums[0] + prev_nums[1])
        return prev_nums[1]