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
        self.nxt = next(self.inorder)

    def next(self) -> int:
        temp = self.nxt
        self.nxt = next(self.inorder,None)
        return temp
        
    def hasNext(self) -> bool:
        return self.nxt != None
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()