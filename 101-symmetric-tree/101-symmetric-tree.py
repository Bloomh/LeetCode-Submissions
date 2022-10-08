# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        leftSide = collections.deque([root.left])
        rightSide = collections.deque([root.right])
        while leftSide and rightSide:
            left = leftSide.popleft()
            right = rightSide.popleft()
            if left and right:
                if not left.val == right.val:
                    return False
                leftSide.append(left.left)
                leftSide.append(left.right)
                rightSide.append(right.right)
                rightSide.append(right.left)
            elif left or right:
                return False
        return not leftSide and not rightSide
        