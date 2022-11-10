class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        for i in range(m-2):
            hrgls = grid[i][0] + grid[i][1] + grid[i][2] + grid[i+2][0] + grid[i+2][1] + grid[i+2][2] + grid[i+1][1]
            ans = max(ans,hrgls)
            for j in range(3,n):
                hrgls += grid[i][j] + grid[i+2][j] - grid[i][j-3] - grid[i+2][j-3] + grid[i+1][j-1] - grid[i+1][j-2]
                ans = max(ans,hrgls)
        return ans