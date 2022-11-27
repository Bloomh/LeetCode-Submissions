@cache
def power(x):
    if x == 1: # base case
        return 1
    elif x % 2: # if x is odd
        return 1 + power(3*x+1) # we need the power of 3*x+1
    else: # if x is even
        return 1 + power(x//2) # we need the power of x//2

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        return sorted(range(lo,hi+1),key=power)[k-1]