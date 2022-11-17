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
        self.inorder = inorder(root) # generator for the inorder traversal of the BST
        self.nxt = next(self.inorder) # get the first value in the traversal

    def next(self) -> int:
        nextval = self.nxt # store the next value
        self.nxt = next(self.inorder,None) # update self.nxt to be the next value in the inorder traversal (or None if there are no more)
        return nextval # return the next value 
        
    def hasNext(self) -> bool:
        return self.nxt != None # if the next value isn't None then we have more values
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()