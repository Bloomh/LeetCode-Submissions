class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        matrix = matrix[::-1]
        while matrix:
            ans.extend(matrix.pop())
            matrix = list(zip(*matrix[::-1]))
        return ans