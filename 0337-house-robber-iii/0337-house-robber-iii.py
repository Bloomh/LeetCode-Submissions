# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        @cache
        def dfs(node, canRob):
            if not node: 
                return 0
            if canRob:
                return max(node.val + dfs(node.left, False) + dfs(node.right, False), dfs(node.left, True) + dfs(node.right, True))
            return dfs(node.left, True) + dfs(node.right, True)
        
        return dfs(root, True)