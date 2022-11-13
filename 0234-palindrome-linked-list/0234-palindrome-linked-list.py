# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        left, right = deque(), deque()
        middle = head.val
        head = head.next
        while head:
            if middle == None:
                middle = right.popleft()
            else:
                left.append(middle)
                middle = None
            right.append(head.val)
            head = head.next
        while left:
            if left.pop() != right.popleft():
                return False
        return True