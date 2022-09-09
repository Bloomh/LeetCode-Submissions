class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        arr = [[[False,False] for i in j] for j in heights]
        q1 = collections.deque([])
        q2 = collections.deque([])
        for i in range(n):
            arr[i][0][0] = True
            q1.append((i,0))
            arr[i][m-1][1] = True
            q2.append((i,m-1))
        for j in range(m):
            arr[0][j][0] = True
            q1.append((0,j))
            arr[n-1][j][-1] = True
            q2.append((n-1,j))

        while q1:
            (r,c) = q1.popleft()
            if arr[r][c][0]:
                for (i,j) in [(r-1,c),(r,c-1),(r+1,c),(r,c+1)]:
                    if 0<=i<n and 0<=j<m and (not arr[i][j][0]) and heights[i][j]>=heights[r][c]:
                        arr[i][j][0] = True
                        q1.append((i,j))
        
        while q2:
            (r,c) = q2.popleft()
            if arr[r][c][1]:
                for (i,j) in [(r-1,c),(r,c-1),(r+1,c),(r,c+1)]:
                    if 0<=i<n and 0<=j<m and (not arr[i][j][1]) and heights[i][j]>=heights[r][c]:
                        arr[i][j][1] = True
                        q2.append((i,j))
        return [(i,j) for i in range(n) for j in range(m) if arr[i][j] == [True,True]]
        