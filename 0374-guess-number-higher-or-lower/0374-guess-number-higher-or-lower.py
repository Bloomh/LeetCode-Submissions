# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l,r = 0,n # left and right pointers 
        while l <= r:
            mid = l+(r-l)//2
            guess_result = guess(mid)
            if guess_result == 0:
                return mid
            elif guess_result == 1:
                l = mid + 1
            else:
                r = mid - 1
        return mid
        