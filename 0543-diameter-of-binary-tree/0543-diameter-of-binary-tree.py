# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0,-1)
            (leftD,leftH),(rightD,rightH) = dfs(node.left),dfs(node.right)
            return (max(leftD,rightD,leftH+rightH+2),max(leftH,rightH)+1)
        return dfs(root)[0]