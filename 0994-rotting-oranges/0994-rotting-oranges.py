class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # store dimensions of grid
        m = len(grid)
        n = len(grid[0])
        
        q = collections.deque() # queue starts with all zeroes
        for i,row in enumerate(grid):
            for j,cell in enumerate(row):
                if cell == 2:
                    q.append((i,j)) # add coords of zeroes
        
        while q: # while there are cells in the queue
            (i,j) = q.popleft() # get the next coords
            for (r,c) in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]: # for all 4-dimensionally adjacent spots
                if 0 <= r < m and  0 <= c < n and (grid[r][c] == 1 or grid[r][c] > grid[i][j]): # if it is in-bounds and mat[r][c] > 0 (meaning it is a 1 and we haven't seen it before) or mat[r][c] < mat[i][j] (meaning we have seen it before but it is closer to a zero than we previously thought)
                    grid[r][c] = grid[i][j] + 1 
                    q.append((r,c)) 
                    
        ans = 0
        # make all the values positive again
        for i,row in enumerate(grid):
            for j,cell in enumerate(row):
                if cell == 1:
                    return -1
                ans = max(ans, cell - 2)
        
        return ans # return matrix