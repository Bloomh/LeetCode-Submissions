class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m > n:
            m,n = n,m
        def product(arr):
            prod = 1
            for num in arr:
                prod *= num
            return prod
        return product(range(m,m+n-1))//product(range(1,n))