"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return None
        stack = [root]
        ans = []
        while stack:
            node = stack.pop()
            ans.append(node.val)
            for i in range(len(node.children)):
                stack.append(node.children[-1-i])
        return ans
    