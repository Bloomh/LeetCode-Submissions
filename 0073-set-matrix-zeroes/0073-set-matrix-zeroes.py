class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = set()
        cols = set()
        for i, row in enumerate(matrix):
            setRow = False
            for j, val in enumerate(row):
                if val == 0:
                    rows.add(i)
                    cols.add(j)
        n = len(matrix[0])
        for i in range(len(matrix)):
            for j in range(n):
                if i in rows or j in cols:
                    matrix[i][j] = 0