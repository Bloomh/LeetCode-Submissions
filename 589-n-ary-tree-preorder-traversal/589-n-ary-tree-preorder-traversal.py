"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root:
            ans = [root.val] # add this node to the preorder traversal
            for node in root.children:
                ans.extend(self.preorder(node)) #add the preorder traversal of each child
            return ans