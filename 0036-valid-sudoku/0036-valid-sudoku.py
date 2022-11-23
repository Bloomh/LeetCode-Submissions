class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for i,row in enumerate(board):
            for j, value in enumerate(row):
                if value != '.':
                    boxNum = 3*(i//3) + j//3
                    if value in rows[i].union(cols[j]).union(boxes[boxNum]):
                        return False
                    rows[i].add(value)
                    cols[j].add(value)
                    boxes[boxNum].add(value)
        return True