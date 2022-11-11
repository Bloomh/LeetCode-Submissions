class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set() # keep track of the numbers we have already seen
        while n != 1: # while n isn't 1
            if n in seen: # if we have seen this number before then we will never reach 1!
                return False
            seen.add(n) # add this number to the one's we've seen
            n = sum(int(dig)**2 for dig in str(n))
        return True