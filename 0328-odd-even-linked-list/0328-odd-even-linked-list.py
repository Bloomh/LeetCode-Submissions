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
        while evens and evens.next: # while the even 
            odds.next = odds.next.next
            evens.next = evens.next.next
            odds = odds.next
            evens = evens.next
        odds.next = firstEven # the last odd should point to the first even
        return firstOdd # return the first odd (the first element in the list)