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
        if n == len(nodes): # if the nth to last node is also the first node
            if n == 1: # if only 1 node
                return None # there is no list remaining after we remove this node
            return nodes[1] # return the second node (we removed the first)
        nodes[-n-1].next = nodes[-n-1].next.next # have the node before the nth from the end point to the node after it! –– this effectively removes the nth node from the end, nodes[-n]
        return nodes[0] # return the first node