# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        this = deque([root])
        nxt = deque([])
        lvl = []
        while this or nxt:
            lvl.append([])
            while this:
                node = this.popleft()
                if not node:
                    continue
                nxt.append(node.left)
                nxt.append(node.right)
                lvl[-1].append(node.val)
            this = nxt
            nxt = deque([])
        lvl.pop()
        return [sum(i)/len(i) for i in lvl]