# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head, prev=None):
        if not head: #if we are past the end of the list
            return prev #return the previous node (this will be the end of the list)

        curr, head.next = head.next, prev #have head.next point to the previous node, update curr to be the next node
        return self.reverseList(curr, head) #reverse the rest of the list