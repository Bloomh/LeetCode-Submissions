class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        def perimeter(i,j):
            ans = 0
            grid[i][j] = 2
            for r,c in [(i-1,j), (i,j-1), (i+1,j), (i,j+1)]:
                if not (0<=r<m and 0<=c<n) or grid[r][c] == 0:
                    ans += 1
                elif grid[r][c] == 1:
                    ans += perimeter(r,c)
            return ans
                        
            
        for i, row in enumerate(grid):
            for j, el in enumerate(row):
                if grid[i][j] == 1:
                    return perimeter(i,j)