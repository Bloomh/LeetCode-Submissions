# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
            
    def __init__(self, root: Optional[TreeNode]):
        def inorder(node):
            if node: # if the node exists
                yield from inorder(node.left) # yield values from the inorder traversal of nodes to the left of it
                yield node.val # yield this value

                yield from inorder(node.right) # yield values from the inorder traversal of nodes to the right of it
        self.inorder = inorder(root)
        self.dq = deque([])

    def next(self) -> int:
        if self.dq:
            return self.dq.pop()
        else:
            return next(self.inorder)
        
    def hasNext(self) -> bool:
        try:
            self.dq.appendleft(next(self.inorder))
            return True
        except:
            return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()