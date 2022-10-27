class Solution:
    def countVowelStrings(self, n: int) -> int:
        return math.factorial(n+4)//math.factorial(n)//24