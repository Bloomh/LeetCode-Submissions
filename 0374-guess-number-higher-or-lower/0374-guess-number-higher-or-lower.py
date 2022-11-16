# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l,r = 0,n # left and right pointers keep track of the range of guesses we are still considering ([l,r] inclusive)
        while l <= r: # while [l,r] still contains valid area to search 
            mid = l+(r-l)//2 # find the middle of the range
            guess_result = guess(mid) # guess the middle
            if guess_result == 1: # if our guess is too small
                l = mid + 1 # then the number must be bigger than mid, so update our range to be [mid+1,r]
            elif guess_result == -1: # if our guess is too big
                r = mid - 1 # then the number must be smaller than mid, so update our range to be [l,mid-1]
            else: # otherwise we guessed right!
                return mid # return the index
        