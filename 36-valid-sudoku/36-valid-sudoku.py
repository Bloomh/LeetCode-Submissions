class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)] #sets for each row
        cols = [set() for _ in range(9)] #sets for each column
        boxes = [set() for _ in range(9)] #sets for each box
        for i in range(len(board)): #go through each row
            for j,num in enumerate(board[i]): #go through each element
                if num == ".": #ignore any blank spaces
                    continue
                boxNumber = (i//3)*3+(j//3) #this is the number box
                if num in rows[i] or num in cols[j] or num in boxes[boxNumber]: #if this is a duplicate in the row, column, or box, then it is an invalid board
                    return False
                rows[i].add(num) #add to the row
                cols[j].add(num) #add to the column
                boxes[boxNumber].add(num) #add to the box
        return True