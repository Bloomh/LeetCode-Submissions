# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode(val=0,next=head) # start.next points to the start of the linked list! – often you will see this called dummy
        slow = start #this will go forward 1 at a time - start 1 spot before the head
        fast = head #move forward 2 at a time
        while fast and fast.next: #while our fast node exists and isn't one of the last two nodes
            slow = slow.next #slow pointer moves forward just 1 spot
            fast = fast.next.next #fast pointer moves forward by two
        slow.next = slow.next.next # slow should be one spot before the middle now, so set it to skip over the next node
        return start.next # return the linked list (remember we set start.next to point to it)