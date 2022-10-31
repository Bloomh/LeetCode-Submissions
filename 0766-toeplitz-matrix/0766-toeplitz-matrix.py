class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        nextrow = matrix[0][:-1] # we need all the elements in the next row (after the first element) to equal all the elements in this row except for the last element
        for row in matrix[1:]: # for all rows except the first one
            for i,num in enumerate(row[1:]): # for all elements in that row except the first one
                if num != nextrow[i]: # if it isn't equal to the corresponding element in our "nextrow"
                    return False # diagonal doesn't line up
            nextrow = [row[0]] + nextrow[:-1] # the last element in "nextrow" gets removed and the first element of this row gets added to the beginning
        return True