class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        mx1 = 0
        mx2 = 0
        mn1 = float('inf')
        mn2 = float('inf')
        for num in nums:
            if num > mx1:
                mx2,mx1 = mx1,num
            elif num > mx2:
                mx2 = num
            if num < mn1:
                mn2,mn1 = mn1,num
            elif num < mn2:
                mn2 = num
        return mx1*mx2-mn1*mn2