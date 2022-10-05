# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while True:
            if root.val > p.val and root.val > q.val: #if the root is bigger than both nodes 
                root = root.left
            elif root.val < p.val and root.val < q.val: #if the root is smaller than both nodes
                root = root.right #both nodes must be to the right of the root
            else:
                return root #otherwise the nodes are on either side of the root or one of the nodes is the root, so we return the root