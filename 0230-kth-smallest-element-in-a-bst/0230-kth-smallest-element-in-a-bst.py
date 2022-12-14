# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node):
            if node: # if the node exists
                yield from inorder(node.left) # yield values from the inorder traversal of nodes to the left of it
                yield node.val # yield this value
                yield from inorder(node.right) # yield values from the inorder traversal of nodes to the right of it
        return next(islice(inorder(root),k-1,k))