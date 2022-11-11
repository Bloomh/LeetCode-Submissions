class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            newN = 0
            while n:
                newN += (n%10)**2
                n //= 10
            n = newN
        return True