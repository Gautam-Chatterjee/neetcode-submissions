# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1,l2,head = list1, list2, ListNode(1)
        h = head
        while l1 and l2:
            if l1.val <= l2.val:
                h.next = l1
                l1 = l1 .next
                h = h.next
            else:
                h.next = l2
                l2 = l2.next
                h = h.next
        
        if l1:
            h.next = l1
        if l2:
            h.next = l2
        
        return head.next







        