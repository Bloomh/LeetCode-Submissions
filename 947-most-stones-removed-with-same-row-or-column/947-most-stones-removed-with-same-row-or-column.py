class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        #THIS IS JUST NUMBER OF PROVINCES --- FIND LOOPS OF STONES AND THEN EACH LOOP HAS TO HAVE ONE STONE REMAINING AT THE END SO IT IS JUST THE TOTAL NUMBER OF STONES MINUS THE NUMBER OF PROVINCES
        n = len(stones)
        numIsl = 0
        def dfs(i,j):
            lst = []
            for (r,c) in stones:
                if r == i or c == j:
                    lst.append([r,c])
            for i in lst:
                stones.remove(i)
            for (r,c) in lst:
                dfs(r,c)
        while stones:
            numIsl += 1
            (i,j) = stones.pop()
            dfs(i,j)
        return n-numIsl