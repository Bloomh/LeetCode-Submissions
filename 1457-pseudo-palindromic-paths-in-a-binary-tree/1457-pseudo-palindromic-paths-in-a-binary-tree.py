# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        def dfs(node, cur):
            if not node: return 0 #none if empty
            cur.remove(node.val) if node.val in cur else cur.add(node.val) #if the node is in the set, remove it. otherwise add it
            res = 0
            if not node.left and not node.right: #if no children
                if len(cur) <= 1: res = 1 #if only one element shows up an odd # of times then we have a result
            else:
                res = res + dfs(node.left, cur) + dfs(node.right, cur) #add results from left and right children
            cur.remove(node.val) if node.val in cur else cur.add(node.val) #undo the action from earlier so the set is not altered for other paths
            return res 
        return dfs(root, set())