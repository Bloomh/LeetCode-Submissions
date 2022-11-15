# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: # if there is no root then there are 0 nodes
            return 0
        
        height = 0 # height of the tree
        node = root # node to find height
        while node: # while the node exists
            height += 1 # add to the height
            node = node.left # move to the left (guaranteed to have a node there if the tree is tall enough)
        lastRow = 2**(height-1) # this is the max number of nodes in the last row (only calculate once)
        
        # find whether or not there are at least "num" many nodes in the bottom row using binary search
        def exists(num):
            node = root # start at the top
            l,r = 0, lastRow # left and right pointers start at 0 and the number of nodes possible
            depth = 0 # keep track of how far down we are
            while depth < height - 1: # while we are not in the last row
                mid = (l+r)//2 # calculate the middle of our range
                if num >= mid: # if the index we are searching for is in the upper half of our range
                    node = node.right # move to the right
                    l = mid + 1 # cut off the left range
                else: # if the index we are searching for is in the lower half of the range
                    node = node.left # move to the left
                    r = mid # cut off the right part of the range
                depth += 1 # we moved further down
            return node != None # return whether or not this node exists
        
        l,r = 0,lastRow-1 # left and right for binary search
        while l <= r: # while there is a region to search
            mid = l+(r-l)//2 # get the middle of the region
            if exists(mid): # if there are at least this many nodes in the last row
                l = mid + 1 # we don't need to check if there are fewer elements
            else: # if there are not that many elements in the last row
                r = mid - 1 # we don't need to check if there are more elements
            
        return lastRow - 1 + l # lastRow - 1 is how many elements are in the rows above the last one, so add the number of elements in the last row (l) to that
            
        
        