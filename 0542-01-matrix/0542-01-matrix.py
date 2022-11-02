class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        q = collections.deque()
        for i,row in enumerate(mat):
            for j,cell in enumerate(row):
                if cell == 0:
                    q.append((i,j))
        
        # make negative if we have seen
        while q:
            (i,j) = q.popleft()
            for (r,c) in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if 0 <= r < m and  0 <= c < n and (mat[r][c] > 0 or mat[r][c] < mat[i][j]):
                    mat[r][c] = mat[i][j] - 1
                    q.append((r,c))
                    
        return [[-num for num in row] for row in mat]