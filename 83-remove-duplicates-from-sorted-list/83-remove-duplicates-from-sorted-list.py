# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = head #points to the front of the linked list
        while head and head.next: #while we aren't at the end of the list
            if head.val == head.next.val: #if the next node has the same value
                head.next = head.next.next #skip it
            else:
                head = head.next #otherwise move forward
        return front #return the front of the linked list