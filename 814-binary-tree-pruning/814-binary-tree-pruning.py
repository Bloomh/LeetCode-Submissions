# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node):
            if not node:
                return False
            l = helper(node.left)
            r = helper(node.right)
            if not l:
                node.left = None
            if not r:
                node.right = None
            return node.val == 1 or l or r
        helper(root)
        return root if root.val==1 or root.left or root.right else None