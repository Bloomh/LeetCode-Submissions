# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: # edge case – check to avoid errors
            return None
        # we will use two pointers to traverse through the even and odd indexed nodes
        # we keep track of the first even node since it needs to be added to our list after the last odd node
        odds = head
        evens = firstEven = head.next
        while evens and evens.next: # while the even pointer exists and is not the last node in the list
            # have both pointers point to the node two ahead of them
            odds.next = odds.next.next 
            evens.next = evens.next.next
            # move each node forward two spots (to the next odd or even indexed node)
            odds = odds.next
            evens = evens.next
        odds.next = firstEven # the last odd node should point to the first even node
        return head # return the head