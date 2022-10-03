# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque([(root,0)])
        ans = []
        while queue:
            node,level = queue.pop()
            if node:
                if level >= len(ans):
                    ans.append([])
                ans[level].append(node.val)
                queue.append((node.right,level+1))
                queue.append((node.left,level+1))
        return ans