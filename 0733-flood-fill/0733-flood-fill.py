class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc] # store the original color we need to fill
        
        if original_color == color: # if the color is the same then we need to do nothing
            return image
        
        m = len(image) # store the number of rows and columns in image
        n = len(image[0])
        
        def fill(i, j): # depth-first-search helper method to fill a square
            image[i][j] = color # set this spot to the color we want
            for (r,c) in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]: # for all 4-dimensionally adjacent spots
                if 0 <= r < m and 0 <= c < n and image[r][c] == original_color: # if the location is in-bounds and is our original color
                    fill(r, c) # fill that square as well
        
        fill(sr, sc)
        return image
            
            
            