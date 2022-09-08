# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = self.inorderTraversal(root.left)
        if ans:
            ans.append(root.val)
        else:
            ans = [root.val]
        r = self.inorderTraversal(root.right)
        if r:
            ans.extend(r)
        return ans