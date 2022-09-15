# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root])
        nxt = deque()
        ans = []
        while q or nxt:
            ans.append(None)
            while q:
                node = q.popleft()
                if not node:
                    continue
                ans[-1] = node.val
                nxt.append(node.left)
                nxt.append(node.right)
            q = nxt
            nxt = deque()       
        return ans[:-1]
            
        