# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head # slow and fast pointers –– fast will be n nodes ahead of slow
        for i in range(n): # n times
            fast = fast.next # move fast forward
        if not fast: # if fast already is at the end then n == len(linkedlist), so remove the first node
            return head.next # return second node in linkedlist
        while fast.next: # while fast is not at the end of the linkedlist
            fast = fast.next # move fast forward
            slow = slow.next # move slow forward
        slow.next = slow.next.next # now skip the nth node from the end
        return head
        