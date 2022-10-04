# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left,right = 0,n #we will look at the range [left,...,right]
        while left<right: #while the range is more than 1 element
            mid = (left+right)//2 #middle of the range
            if isBadVersion(mid): #if this is a bad version then we want this to be the last possible index in our range
                right = mid #stop looking after mid
            else: #if it is not a bad version then we need to look at versions after this one (so we start looking at mid+1)
                left = mid+1
        return left
            