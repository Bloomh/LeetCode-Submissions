# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node,minimum,maxmimum): #helper method -- check if 
            if not node:
                return True
            if not minimum<node.val<maxmimum:
                return False
            return validate(node.left,minimum,node.val) and validate(node.right,node.val,maxmimum)
        return validate(root,float('-inf'),float('inf'))