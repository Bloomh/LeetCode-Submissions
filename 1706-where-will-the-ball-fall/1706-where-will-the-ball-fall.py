class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        def route(i,j):
            if i>=len(grid):
                return j
            g = grid[i][j]
            if (g == 1 and (j==len(grid[0])-1 or grid[i][j+1]==-1)) or (g == -1 and (j==0 or grid[i][j-1]==1)):
                return -1
            return route(i+1,j+g)
        return [route(0,x) for x in range(len(grid[0]))]
                