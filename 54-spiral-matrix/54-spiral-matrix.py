class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        right = len(matrix[0])
        left = 0
        bottom = len(matrix)
        ans = []
        while top<bottom and left<right:
            for i in range(left,right):
                ans.append(matrix[top][i])
            top +=1
            if top==bottom:
                break
            for i in range(top,bottom):
                ans.append(matrix[i][right-1])
            right -=1
            if right==left:
                break
            for i in range(right-1,left-1,-1):
                ans.append(matrix[bottom-1][i])
            bottom -=1
            if top==bottom:
                break
            for i in range(bottom-1,top-1,-1):
                ans.append(matrix[i][left])
            left +=1
        return ans