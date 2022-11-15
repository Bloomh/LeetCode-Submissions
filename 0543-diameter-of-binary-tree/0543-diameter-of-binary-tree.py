# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node): # helper method to find the height of a node
            if not node: # empty nodes will be considered to have diameter and height of 0 and
                return (0,0)
            (left_diameter,left_height) = dfs(node.left) # get the diameter and height of the left subnode
            (right_diameter,right_height) = dfs(node.right) # get the diameter and height of the right subnode
            return (max(left_diameter,right_diameter,left_height+right_height), max(left_height,right_height)+1) # return the maximum diameter and the height of this node
        return dfs(root)[0] # return the maximum diameter