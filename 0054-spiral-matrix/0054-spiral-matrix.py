class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        while matrix:
            ans.extend(matrix.pop(0))
            matrix = list(zip(*matrix))[::-1]
        return ans