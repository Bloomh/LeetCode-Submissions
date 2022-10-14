# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        runner = head #runner to find the length of the linked list
        length = 0 #length of list
        while runner:
            length += 1 #add 1 to the length whenever we still have a node
            runner = runner.next
        runner = head # reset the runner back to the head
        if length == 1: # once again if there is only one node, the list becomes empty
            return None
        for i in range(length//2-1): #go halfway through the linked list
            runner = runner.next
        runner.next = runner.next.next # skip the next node (the middle node)
        return head #return the middle node