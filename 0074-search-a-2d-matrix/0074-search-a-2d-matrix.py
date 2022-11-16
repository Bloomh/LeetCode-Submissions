class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l,r = 0, n*m
        while l < r:
            mid = l+(r-l)//2
            element = matrix[mid//n][mid%n]
            if element > target:
                r = mid
            elif element < target:
                l = mid + 1
            else:
                return True
        return False