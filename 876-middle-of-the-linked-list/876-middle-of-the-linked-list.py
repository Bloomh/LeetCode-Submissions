# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        runner = head #runner to find the length of the linked list
        length = 0 #length of list
        while runner:
            length += 1 #add 1 to the length whenever we still have a node
            runner = runner.next
        for i in range(length//2): #go halfway through the linked list
            head = head.next
        return head #return the middle node