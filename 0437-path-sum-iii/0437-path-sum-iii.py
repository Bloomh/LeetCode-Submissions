# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.ans = 0
        def pathSums(node):
            sums = defaultdict(int)
            if node:
                for key,val in pathSums(node.left).items():
                    sums[key+node.val] += val
                for key,val in pathSums(node.right).items():
                    sums[key+node.val] += val
                sums[node.val] += 1
                self.ans += sums[targetSum]
            return sums
        
        pathSums(root)
        return self.ans