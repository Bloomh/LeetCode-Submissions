# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set() # set of nodes we have seen
        def dfs(node): # helper dfs method
            if node:
                if node.val in seen: # if have needed this value before
                    return True # we can sum to k
                seen.add(k - node.val) # add the number needed to sum to k to our set
                return dfs(node.left) or dfs(node.right) # check the left and the right
        return dfs(root) # check the whole tree