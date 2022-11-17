# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node):
            if node:
                return inorder(node.left)+[node.val]+inorder(node.right)
            return []
        inorder_traversal = inorder(root)
        return inorder_traversal[k-1]