class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        l, r = 0, n*m
        while l<r:
            mid = l+(r-l)//2
            el = matrix[mid//m][mid%m]
            if el == target:
                return True
            elif el < target:
                l = mid+1
            else:
                r = mid
        return False