class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        # first we store the dimensions of the grid to use later
        m = len(grid)
        n = len(grid[0])

        # helper method to determine where a ball dropped at grid[i][j] will fall
        def path(i,j):
            direction = grid[i][j] # the direction the ball will go (1 if slanted right, -1 if slanted left)
            j += direction # move in that direction
            # since the ball is now at a new index grid[i][j] (j changed), we need to check if 0 <= j < n (the ball will be in-bounds – otherwise it gets stuck on a wall)
            # We also need to check that grid[i][j] is the same as our original direction since otherwise, we have a V shape which traps the ball
            if not (0 <= j < n and direction == grid[i][j]):  # if we don't meet these conditions we get trapped
                return -1
            if i == m-1: # if we are at the bottom row
                return j # return our resultant column
            return path(i+1, j) # move down one row and repeat the process!

        return map(lambda x:path(0,x), range(n))