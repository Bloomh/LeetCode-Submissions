class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        while columnNumber > 0:
            rem = columnNumber % 26
            columnNumber //= 26
            if rem == 0:
                rem = 26
                columnNumber -= 1
            ans = chr(rem+64) + ans
        return ans