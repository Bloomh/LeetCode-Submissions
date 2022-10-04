# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def dfs(node,amt):
            if node:
                if not node.left and not node.right:
                    self.ans += amt*10+node.val
                amt = amt*10+node.val
                dfs(node.left,amt)
                dfs(node.right,amt)
        
        dfs(root,0)
        
        return self.ans