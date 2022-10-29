# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = [] # keep track of the nodes
        while head: # while looking at a node
            nodes.append(head) # add this node to our list
            head = head.next # move to the next node
        nodes.append(None) # add None to the end of our list to deal with the n == 1 case more easily
        if n == len(nodes) - 1: # if the nth to last node is also the first node
            return nodes[1] # return the second node (we removed the first)
        nodes[-n-2].next = nodes[-n] # have the node before the nth from the end point to the node after it! –– this effectively removes the nth node from the end, nodes[-n-1
        return nodes[0] # return the first node