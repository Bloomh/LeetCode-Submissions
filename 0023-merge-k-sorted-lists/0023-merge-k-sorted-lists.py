# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def search(self, arr, target):
        l,r = 0,len(arr)
        while l<r:
            m = l+(r-l)//2
            val = arr[m].val
            if val == target:
                return m
            elif val < target:
                r = m
            else:
                l = m + 1
        return l
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        start = curr = ListNode()
        lists = sorted([i for i in lists if i is not None], key = lambda x:x.val, reverse = True)
        # print([i.val for i in lists])
        while lists:
            first = lists.pop()
            curr.next = first
            curr = curr.next
            first = first.next
            if first is not None:
                lists.insert(self.search(lists,first.val),first)
        return start.next