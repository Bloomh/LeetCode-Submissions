class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        searched = {}
        def dfs(i):
            searched[i] = True
            for j in range(len(isConnected[i])):
                if isConnected[i][j] and j not in searched:
                    dfs(j)

        ans = 0
        for i in range(len(isConnected)):
            if i in searched:
                continue
            else:
                ans += 1
                dfs(i)
        return ans
            