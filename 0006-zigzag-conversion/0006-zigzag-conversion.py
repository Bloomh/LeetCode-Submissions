class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        n = len(s)
        ans = s[::numRows*2-2] # start with the top row
        for row in range(1,numRows-1): # get the middle rows
            i = row # start at this row's first character
            increment = numRows*2 - 2 - row*2 # this is how far away the next character in this row is
            while i < n: # while in bounds
                ans += s[i] # add this element
                i += increment # jump to the next element in this row
                increment = numRows*2 - 2 - increment # increment changes each time
        return ans + s[numRows-1::numRows*2-2] # add the bottom row
            
            