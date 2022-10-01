# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = [] #keep track of the nodes
        while head:
            if head in nodes: #if the head is already in our list then we have a cycle
                return head
            nodes.append(head) #add node to our list
            head = head.next
        return None #no cycle found!