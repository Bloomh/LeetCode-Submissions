# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = [] # answer

        def dfs(node): # depth-first-search helper method
            if node: # we only care about nodes that exist
                dfs(node.left) # add the preorder traversal of the left node
                self.ans.append(node.val) # add this node to the traversal
                dfs(node.right) # add the preorder traversal of the right node

        dfs(root) # start at the top
        return self.ans