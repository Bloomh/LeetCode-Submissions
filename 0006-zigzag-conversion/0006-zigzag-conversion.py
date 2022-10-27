class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        n = len(s)
        ans = s[::numRows*2-2]
        for row in range(1,numRows-1):
            i = row
            increment = numRows*2 - 2 - row*2
            while i < n:
                ans += s[i]
                i += increment
                increment = numRows*2 - 2 - increment
        return ans + s[numRows-1::numRows*2-2]
            
            