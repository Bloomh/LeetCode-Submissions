# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        fast = h = head
        for i in range(n+1):
            try:
                fast = fast.next
            except:
                return head.next
        while fast:
            head = head.next
            fast = fast.next
        head.next = head.next.next
        return h