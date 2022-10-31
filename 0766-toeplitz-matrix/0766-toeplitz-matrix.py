class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        nextrow = [num for i,num in enumerate(matrix[0][:-1])]
        for row in matrix[1:]:
            for i,num in enumerate(row[1:]):
                if num != nextrow[i]:
                    return False
            nextrow = [row[0]] + nextrow[:-1]
        return True