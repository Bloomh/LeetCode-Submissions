class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        
        def path(i,j):
            direction = grid[i][j]
            if not (0 <= j + direction < n and direction == grid[i][j+direction]):
                return -1
            if i == m-1:
                return j + direction
            return path(i+1, j+direction)
        
        return [path(0,i) for i in range(n)]