# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,node): #dfs
        if not node:
            return 0
        left = self.dfs(node.left)
        if left < 0:
            left = 0
        right = self.dfs(node.right)
        if right < 0:
            right = 0
        if node.val + right + left > self.ans:
            self.ans = node.val + right + left
        if right < left:
            right = left
        return node.val + right
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = float('-inf') #answer  
        self.dfs(root) #dfs on root
        return self.ans

        
            
        