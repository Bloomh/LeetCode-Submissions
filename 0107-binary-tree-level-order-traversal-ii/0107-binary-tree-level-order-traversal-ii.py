# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque([(root,0)]) #queue of nodes to look at
        ans = [] #answer queue
        while queue: #while we have nodes to look at
            node,level = queue.popleft() #get the next node and its level
            if node: #we only care if there is a node --> it may be None, which we want to avoid
                if level >= len(ans): #if there arent enough levels in our array
                    ans = [[]] + ans #add a new level at the start
                ans[-level-1].append(node.val) #add this value to the level (level goes from the back of the array since it is in reverse)
                queue.append((node.left,level+1)) #add left child to queue
                queue.append((node.right,level+1)) #add right child to queue
        return ans # reverse result