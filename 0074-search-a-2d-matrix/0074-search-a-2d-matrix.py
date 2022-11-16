class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l,r = 0, n*m-1
        while l <= r:
            mid = l+(r-l)//2
            element = matrix[mid//n][mid%n]
            print(element)
            if element > target:
                r = mid - 1
            elif element < target:
                l = mid + 1
            else:
                return True
        return False