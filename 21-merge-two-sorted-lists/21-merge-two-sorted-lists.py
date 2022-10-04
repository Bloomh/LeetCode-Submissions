# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def printList(self, node,i=None):
        lst = []
        while node:
            lst.append(node.val)
            node = node.next
        if i:
            lst = lst[:i]
        print(lst, end = "")
        
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start = curr = ListNode(0) #an empty node at the start – curr will go through all the nodes in the joint list while start will point to the beginning of the list
        i = 0
        while list1 and list2: #while both lists exist
            print('Sorted list: ', end='')
            self.printList(start.next,i)
            print(', Remainder of list1: ', end='')
            self.printList(list1)
            print(', Remainder of list2: ', end='')
            self.printList(list2)
            print()
            if list1.val <= list2.val: #if list1 has the smaller value (or equal)
                print('list1 has smaller value so that is next in the list')
                curr.next = list1 #make it the next node in the list
                list1 = list1.next #move forward in the list
            else: #otherwise do the same but with list2
                print('list2 has smaller value so that is next in the list')
                curr.next = list2 
                list2 = list2.next
            curr = curr.next #move forward in the joint list
            i+=1
            print()
        print('Sorted list: ', end='')
        self.printList(start.next,i)
        print()
        print('add remaining nodes')
        curr.next = list1 or list2 #point to whichever list is remaining
        print('Final sorted list: ', end='')
        self.printList(start.next)
        return start.next #return the joint list (start points to it)