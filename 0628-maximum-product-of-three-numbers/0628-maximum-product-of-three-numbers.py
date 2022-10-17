class Solution:
    from heapq import nlargest, nsmallest
    def maximumProduct(self, nums: List[int]) -> int:
        big = nlargest(3,nums)
        small = nsmallest(2,nums)
        return max(big[2]*big[1]*big[0],small[0]*small[1]*big[0])