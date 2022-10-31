"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue = collections.deque([(0,root)])
        while queue:
            (level, node) = queue.popleft()
            if node:
                queue.append((level+1,node.left))
                queue.append((level+1,node.right))
                if queue and queue[0][0] == level:
                    node.next = queue[0][1]
        return root