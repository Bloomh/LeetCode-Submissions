# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head #slow pointer
        fast = head #fast poiner
        while fast and fast.next: #while fast is not at the end of the list
            slow = slow.next
            fast = fast.next.next
            if slow == fast: #if we encountered a cycle
                while head!=slow: #move head and slow forward until they meet
                    head = head.next
                    slow = slow.next
                return slow #this is the start of the cycle!
        return None #no cycle