# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head #this will go forward 1 at a time
        fast = head #move forward 2 at a time
        while fast and fast.next: #while our fast node exists and isn't the last node
            slow = slow.next #slow pointer moves forward just 1 spot
            fast = fast.next.next #fast pointer moves forward by two
        return slow #slow should be in the middle!