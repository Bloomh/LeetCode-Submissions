# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0 # length
        runner = head # runner to find length
        while runner: # while the runner exists
            length += 1 # add to the length
            runner = runner.next # go to the next node
        if length == n: # if we need to remove the first node
            return head.next # remove it by returning the next node
        runner = head # reset our runner
        for i in range(length - n - 1): # until there are n nodes left in the linkedlist
            runner = runner.next # move forward in the linkedlist
        runner.next = runner.next.next # skip the next node (nth from the end)
        return head # return the head
        
        