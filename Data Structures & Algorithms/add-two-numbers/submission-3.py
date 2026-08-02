# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new = ListNode()
        carry = 0
        curr = new
        while l1 and l2:
            sm = l1.val + l2.val + carry
            carry = 1 if sm >= 10 else 0
            new_node = ListNode(sm%10)
            curr.next = new_node
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            sm = l1.val + carry
            carry = 1 if sm >= 10 else 0
            new_node = ListNode(sm%10)
            curr.next = new_node
            curr=curr.next
            l1= l1.next
        
        while l2:
            sm = l2.val + carry
            carry = 1 if sm >= 10 else 0
            new_node = ListNode(sm%10)
            curr.next = new_node
            curr=curr.next
            l2=l2.next
        
        if carry == 1:
            new_node = ListNode(1)
            curr.next = new_node
        
        return new.next
            
        



            
        