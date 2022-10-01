class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)] #
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for i in range(len(board)):
            for j,num in enumerate(board[i]):
                if num == ".":
                    continue
                boxNumber = (i//3)*3+(j//3)
                if num in rows[i] or num in cols[j] or num in boxes[boxNumber]:
                    return False
                rows[i].add(num)
                cols[j].add(num)
                boxes[boxNumber].add(num)
        return True