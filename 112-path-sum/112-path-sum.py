# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: #if no root given then there is no pathsum
            return False
        if not root.left and not root.right: #if this is a leaf
            return targetSum == root.val #see if this is the number we need
        left = self.hasPathSum(root.left,targetSum-root.val) #see if we can make the pathsum with the left subtree
        right = self.hasPathSum(root.right,targetSum-root.val) #check right subtree
        return left or right #return 