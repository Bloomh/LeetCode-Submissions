# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            if not node:
                return 1
            l = helper(node.left)
            r = helper(node.right)
            if l==False or r==False:
                return False
            return False if abs(l-r)>1 else max(l,r)+1
        return helper(root)!=False