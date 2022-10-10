# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return TreeNode(val) if not root else TreeNode(root.val, root.left, self.insertIntoBST(root.right,val)) if root.val < val else TreeNode(root.val, self.insertIntoBST(root.left,val), root.right)