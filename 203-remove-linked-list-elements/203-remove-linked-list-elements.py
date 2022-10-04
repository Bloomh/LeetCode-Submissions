# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head: #if there is no list then we do nothing
            return None
        front = head #point to the new front of the head
        while head and head.val == val: #while the first node is equal to the value
            front = front.next #skip over it 
            head = head.next #move forward
        while head and head.next: #while we aren't at the end of the list
            if head.next.val == val: #while the next node equals the value to remove
                head.next = head.next.next #skip over it!
            else: #otherwise
                head = head.next #move forward
        return front #return the pointer to the front of the list