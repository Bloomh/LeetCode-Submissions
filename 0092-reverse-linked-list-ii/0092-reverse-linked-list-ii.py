# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def printll(self,ll):
        n = []
        while ll:
            n.append(ll.val)
            ll = ll.next
        print(n)
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        h = ListNode(0, head)
        pre = h
        i = 0
        while i < left - 1:
            head = head.next
            pre = pre.next
            i += 1
        prev = None
        leftNode = head
        while i < right:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
            i += 1
        pre.next = prev
        leftNode.next = head
        return h.next