# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return all(vals[i] == vals[-i-1] for i in range(len(vals)//2))