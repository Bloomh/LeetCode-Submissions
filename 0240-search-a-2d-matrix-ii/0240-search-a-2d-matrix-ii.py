class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        row,col = 0,n-1
        while row < m and 0 <= col:
            element = matrix[row][col]
            if element > target:
                col -= 1
            elif element < target:
                row += 1
            else:
                return True
        return False