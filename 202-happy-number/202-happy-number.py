class Solution:
    def isHappy(self, n: int) -> bool:
        def cyc(num):
            ans = 0
            while num:
                ans+=(num%10)**2
                num//=10
            return ans
        hist = []
        while n!=1:
            if n in hist:
                return False
            hist.append(n)
            n = cyc(n)
        return True