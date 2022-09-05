"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return None
        ans = []
        ths = collections.deque([root])
        nxt = collections.deque([])
        while ths or nxt:
            ans.append([])
            while ths:
                node = ths.popleft()
                if node.children:
                    for i in node.children:
                        nxt.append(i)
                ans[-1].append(node.val)
            ths = nxt
            nxt = collections.deque([])
        return ans
        