class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        ans = 0
        for i in range(1,min(a,b)+1):
            if a%i == 0 == b%i:
                ans += 1
        return ans