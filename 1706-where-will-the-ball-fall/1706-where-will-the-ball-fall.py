class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        
        def path(i,j):
            direction = grid[i][j]
            j += direction
            if not (0 <= j < n and direction == grid[i][j]):
                return -1
            if i == m-1:
                return j
            return path(i+1, j)
        
        return [path(0,i) for i in range(n)]