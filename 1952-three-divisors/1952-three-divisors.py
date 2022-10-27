class Solution:
    def isThree(self, n: int) -> bool:
        div = 0
        for i in range(1,n+1):
            div += (n%i == 0)
        return div == 3