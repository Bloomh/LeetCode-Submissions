# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def checkSymmetry(left,right):
            if left and right and left.val == right.val:
                return checkSymmetry(left.left,right.right) and checkSymmetry(left.right,right.left)
            return not left and not right
        return checkSymmetry(root.left, root.right)
        