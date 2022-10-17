# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode, mx = float('-inf')) -> int:
        if root:
            if root.val >= mx:
                return 1 + self.goodNodes(root.left, root.val) + self.goodNodes(root.right, root.val)
            return self.goodNodes(root.left, mx) + self.goodNodes(root.right, mx)
        return 0