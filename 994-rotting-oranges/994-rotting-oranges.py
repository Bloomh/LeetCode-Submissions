class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        n = len(grid)
        m = len(grid[0])
        numFresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    numFresh += 1
        ans = 0
        while q:
            ans += 1
            didnt = -1
            nq = []
            for (r,c) in q:
                for (i,j) in [(r-1,c),(r,c-1),(r+1,c),(r,c+1)]:
                    if 0<=i<n and 0<=j<m and grid[i][j] == 1:
                        didnt = 0
                        grid[i][j] = 2
                        numFresh -= 1
                        nq.append((i,j))
            q = nq
            ans += didnt
            
        if numFresh > 0:
            return -1
        return ans