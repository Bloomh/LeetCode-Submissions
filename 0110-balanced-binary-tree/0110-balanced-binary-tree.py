# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # helper method to determine the height of a node
        # however it will return False if the tree beginning at node is not height-balanced
        def dfs(node):
            if not node: # if there is no node then return 1
                return 1 # this will be our lowest height
            left, right = dfs(node.left), dfs(node.right) # get the height of the left and right subtrees
            # if either subtree is NOT height balanced, then the whole tree is not height-balanced
            if left == False or right == False or abs(left-right)>1: # if the heights of the subtrees are not within 1 of each other, then the tree isn't height balanced
                return False
            return max(left,right) + 1 # the height of this tree is 1 more than the maximum height of the subtrees
        return dfs(root) != False # if we never returned False then we never found a height-balancing issue!