# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @lru_cache
    def dfs(self,node,trg):
        ans = 0
        if not node:
            return 0
        if node.val == trg:
            ans += 1
        ans += self.dfs(node.left,trg-node.val)
        ans += self.dfs(node.right,trg-node.val)
        return ans
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        return self.dfs(root,targetSum) + self.pathSum(root.left,targetSum) + self.pathSum(root.right,targetSum)