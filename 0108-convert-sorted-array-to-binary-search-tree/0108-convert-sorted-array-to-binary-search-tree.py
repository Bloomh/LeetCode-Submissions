# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def arrToBST(left, right): # 
            if right >= left:
                mid = left+(right-left)//2
                return TreeNode(nums[mid],arrToBST(left,mid-1),arrToBST(mid+1,right))
        return arrToBST(0,len(nums)-1)