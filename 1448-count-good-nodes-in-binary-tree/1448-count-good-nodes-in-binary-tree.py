# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(node, highest):
            ans = 0
            if not node:
                return ans
            if node.val>=highest:
                ans += 1
                highest = node.val
            return ans + helper(node.left,highest) + helper(node.right,highest)
        return helper(root,-float('inf'))
        