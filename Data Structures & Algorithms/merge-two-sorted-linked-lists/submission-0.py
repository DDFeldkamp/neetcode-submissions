# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        first = ListNode(0)
        rest = first
        while list1 and list2:
            if list1.val < list2.val:
                list1, rest.next = list1.next, list1
            else: 
                list2, rest.next = list2.next, list2
            rest = rest.next
        if list1:
            rest.next = list1
        else:
            rest.next = list2
        return first.next
        