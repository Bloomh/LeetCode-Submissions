# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 1
            left, right = dfs(node.left), dfs(node.right)
            if left == False or right == False or abs(left-right)>1:
                return False
            return max(left,right) + 1
        return dfs(root) != False