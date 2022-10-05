# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1: #extra case
            return TreeNode(val,root) #val is the value of the new root, left points to original tree
            
        queue = collections.deque([(root,depth)]) #queue for bfs starts with the root
        while queue: #while there are nodes to look at
            node,depth = queue.popleft() #get the next node
            if node: #if the node exists
                if depth == 2: #if we need to add the nodes to the next level
                    node.left = TreeNode(val,node.left) #add left
                    node.right = TreeNode(val,None,node.right) #add right
                else: #otherwise go to the next level
                    queue.append((node.left,depth-1)) #add the left child
                    queue.append((node.right,depth-1)) #add the right child
                    
        return root #return the new tree