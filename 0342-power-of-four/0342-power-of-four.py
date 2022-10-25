class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        b = bin(n)[::-1]
        return n > 0 and b.count("1") == 1 and b.index("1") % 2 == 0