class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        def searchIsland(r,c):
            grid[r][c] = "2"
            for (row,col) in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                if 0 <= row < m and 0 <= col < n and grid[row][col] == "1":
                    searchIsland(row,col)
        
        ans = 0
        for i, row in enumerate(grid):
            for j, element in enumerate(row):
                if element == "1":
                    searchIsland(i,j)
                    ans += 1
        return ans