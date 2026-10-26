# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(prev, curr):
            if not curr:
                return prev
            else:
                return helper(ListNode(curr.val, prev), curr.next)
        return helper(None, head)
            
