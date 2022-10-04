class Solution:
    def countHousePlacements(self, n: int) -> int:
        if n == 1:
            return 4
        one = 3
        two = 2
        for i in range(2,n):
            one,two = one+two,one
        return one**2 % (10**9+7)