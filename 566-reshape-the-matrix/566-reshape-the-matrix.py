class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        if n*m!=r*c: #if the total number of elements in the original matrix wouldn't fit into a r by  c matrix
            return mat #return original
        ans = [[0 for i in range(c)] for j in range(r)] #new empty matrix
        num = 0 #keep track of how many elements we have added to our new array
        for i in range(n): #iterating through mat
            for j in range(m):
                row = num//c #the row we are writing into
                col = num%c #the column we are writing into
                ans[row][col] = mat[i][j] #add this element to the row in ans
                num+=1 #we added the last element
        return ans