class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        if n*m!=r*c: #if the total number of elements in the original matrix wouldn't fit into a r by  c matrix
            return mat #return original
        ans = [] #new matrix
        num = 0 #keep track of how many elements we have added to our new array
        for i in range(r):
            ans.append([]) #add a new row
            for j in range(c):
                row = num//m #the row we are accessing
                col = num%m #the column we are accessing
                ans[i].append(mat[row][col]) #add this element to the row in ans
                num+=1 #we added the last element
        return ans