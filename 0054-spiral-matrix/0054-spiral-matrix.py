class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bot, lft, rght = 0, len(matrix), 0, len(matrix[0]) # keep track of the top, bottom, left, and right of the region we are considering
        ans = [] # empty matrix
        
        while top < bot and lft < rght: # while we still have area to cover
            ans.extend(matrix[top][lft:rght]) # add the top row
            top += 1 # the top of our range gets lower (by increasing index)
            if top == bot:
                return ans
            ans.extend([matrix[row][rght-1] for row in range(top,bot)]) # add the rightmost column
            rght -= 1 # rightmost column becomes smaller index
            if rght == lft:
                return ans
            
            ans.extend(matrix[bot-1][lft:rght][::-1]) # add the bottom row in reverse order (right to left)
            bot -= 1 # bottom row is now a smaller index
            ans.extend([matrix[row][lft] for row in range(bot-1,top-1,-1)]) # add the leftmost column in reverse order (bottom to top)
            lft += 1
            
            
        
        return ans