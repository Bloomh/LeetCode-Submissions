# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.left = 0
        self.right = 0
        ans = [[]]
        def helper(r,c,node):
            if node:
                if c < self.left:
                    ans.insert(0,[])
                    self.left -= 1
                elif c > self.right:
                    ans.append([])
                    self.right += 1
                ans[c-self.left].append((r,node.val))
                helper(r+1,c+1,node.right)
                helper(r+1,c-1,node.left)
        helper(0,0,root)
        for i in ans:
            i.sort(key=lambda x:(x[0],x[1]))
        return [[i[1] for i in j] for j in ans]