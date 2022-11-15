# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0 # keep track of the diameter
        def dfs(node): # helper method to find the height of a node
            if not node: # empty nodes will be considered to have height of 0
                return 0
            left,right = dfs(node.left),dfs(node.right) # get the height of the left and the right subnodes
            self.diameter = max(self.diameter, right+left) # the maximum diameter could be the left height + the right height – update if necessary
            return max(left,right)+1 # return the height of this node (one greater than the height of the subnodes)
        dfs(root) # go through the nodes 
        return self.diameter # return the maximum diameter