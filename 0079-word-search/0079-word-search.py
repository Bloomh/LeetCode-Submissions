class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        wordLength = len(word)
        def helper(row,col,index):
            if board[row][col] == word[index]:
                if index == wordLength-1:
                    return True
                board[row][col] = ord(board[row][col])
                for (i,j) in [(row-1,col), (row,col-1), (row+1,col), (row,col+1)]: 
                    if 0<=i<m and 0<=j<n and helper(i,j,index+1):
                        return True
            else: 
                return False
            board[row][col] = chr(board[row][col])
            return False

        for i in range(m):
            for j in range(n):
                if helper(i,j,0):
                    return True
        return False