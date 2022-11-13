# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        odds = firstOdd = head
        evens = firstEven = head.next
        while evens and evens.next:
            odds.next, evens.next = odds.next.next, evens.next.next
            odds, evens = odds.next, evens.next
        odds.next = firstEven
        return firstOdd