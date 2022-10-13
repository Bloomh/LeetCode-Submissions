# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.ans = [] # answer
        def dfs(node,level): # node and level it is on
            if node: # we only care if the node exists
                if level >= len(self.ans): # if we need to add another level
                    self.ans = [[]] + self.ans # add new row to the beginning
                self.ans[-level-1].append(node.val) # add this to the corresponding level
                dfs(node.left,level+1) # check left subtree
                dfs(node.right,level+1) # check right subtree
        dfs(root,0) # search tree
        return self.ans # reverse result