class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        swapped = set()
        
        def swap(self, i, j):
            matrix[j][n-i-1], matrix[n-i-1][n-j-1], matrix[n-j-1][i], matrix[i][j] = matrix[i][j], matrix[j][n-i-1], matrix[n-i-1][n-j-1], matrix[n-j-1][i]
            
            swapped.update([(i,j), (j,n-i-1), (n-i-1,n-j-1), (n-j-1, i)])
        
        for i in range(n):
            for j in range(n):
                if (i,j) not in swapped:
                    swap(self,i,j)