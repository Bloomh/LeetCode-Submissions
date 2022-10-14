# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = [] #array to keep track of the nodes
        while head:
            nodes.append(head) #add the nodes to our array
            head = head.next
        if len(nodes) == 1: # if there is only one node then the linked list becomes empty
            return None
        middle = len(nodes)//2 # middle index
        if middle == len(nodes) - 1: # if the middle node is also the last node
            nodes[middle-1].next = None # then we have the node before it point to None
        else:
            nodes[middle-1].next = nodes[middle+1] # have the node before the middle point to the node after the middle
        return nodes[0] # return the head of the list