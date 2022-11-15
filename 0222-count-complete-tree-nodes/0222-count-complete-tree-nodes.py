# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        height = 0 # height of the tree
        node = root # node to find height
        while node: # while the node exists
            height += 1 # add to the height
            node = node.left # move to the left (guaranteed to have a node there if the tree is tall enough)
        lastRow = 2**(height-1)
        # find whether or not there are at least "num" many nodes in the bottom row
        def exists(num):
            node = root
            l,r = 0, lastRow
            depth = 0
            while depth < height - 1:
                mid = (l+r)//2
                print(node.val,mid)
                if num >= mid:
                    node = node.right
                    l = mid + 1
                else:
                    node = node.left
                    r = mid
                depth += 1
            return node != None
        
        l,r = 0,lastRow-1
        while l <= r:
            mid = l+(r-l)//2
            if exists(mid):
                l = mid + 1
            else:
                r = mid - 1
            
        return lastRow - 1 + l
            
        
        