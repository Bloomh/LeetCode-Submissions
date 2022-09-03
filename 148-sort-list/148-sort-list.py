# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        nodes.sort(key=lambda x:x.val)
        nodes.append(None)
        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]
        return nodes[0]