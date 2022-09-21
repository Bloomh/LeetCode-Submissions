class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle)
        ans = 0
        for i in columnTitle:
            n-=1
            ans+= 26**n*(ord(i)-64)
        return ans