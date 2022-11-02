class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # store dimensions of mat
        m = len(mat)
        n = len(mat[0])
        
        q = collections.deque() # queue starts with all zeroes
        for i,row in enumerate(mat):
            for j,cell in enumerate(row):
                if cell == 0:
                    q.append((i,j)) # add coords of zeroes
        
        while q: # while there are cells in the queue
            (i,j) = q.popleft() # get the next coords
            for (r,c) in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]: # for all 4-dimensionally adjacent spots
                if 0 <= r < m and  0 <= c < n and (mat[r][c] > 0 or mat[r][c] < mat[i][j]): # if it is in-bounds and mat[r][c] > 0 (meaning it is a 1 and we haven't seen it before) or mat[r][c] < mat[i][j] (meaning we have seen it before but it is closer to a zero than we previously thought)
                    mat[r][c] = mat[i][j] - 1 # set it to mat[i][j] - 1 --> we will use negative numbers to keep track of the elements we have already seen (rather than using a visited set)
                    q.append((r,c)) # add this to the queue since we need to look around this spot
        # make all the values positive again
        for i,row in enumerate(mat):
            for j,cell in enumerate(row):
                mat[i][j] = -cell
        
        return mat # return matrix