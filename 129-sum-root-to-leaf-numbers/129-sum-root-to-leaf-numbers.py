# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0 #answer
        
        def dfs(node,amt): #depth-first search helper method
            if node: #we only care if there is a node
                amt = amt*10+node.val #update the corresponding amount for this root-to-leaf path
                if not node.left and not node.right: #if it is a leaf
                    self.ans += amt #then add the path to our answer
                else: #if it isn't a leaf
                    dfs(node.left,amt) #search to the left
                    dfs(node.right,amt) #search to the right
        
        dfs(root,0) #perform dfs on the root
        
        return self.ans #return answer