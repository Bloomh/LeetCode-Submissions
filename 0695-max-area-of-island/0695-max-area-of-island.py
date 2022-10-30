class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # start by storing the number of rows and columns in the grid for later
        m = len(grid)
        n = len(grid[0])
        
        # helper method to calculate the area of an island
        def areaOfIsland(i, j):
            area = 1 # there is at least 1 cell in this island
            grid[i][j] = 2 # set this cell to to avoid searching it again
            for (r, c) in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]: # go through all 4 dimensionally adjacent squares
                if 0 <= r < m and 0 <= c < n and grid[r][c] == 1: # if the cell is in-bounds and is land
                    area += areaOfIsland(r, c) # add the area of this region to the area of our island
            return area
            
        ans = 0 # default answer is 0
        for i, row in enumerate(grid): # go through all rows
            for j, cell in enumerate(row): # go through all cells in the row
                if cell == 1: # if we encountered land
                    ans = max(ans, areaOfIsland(i, j)) # compare the area of this island with our answer, update if needed       
        return ans