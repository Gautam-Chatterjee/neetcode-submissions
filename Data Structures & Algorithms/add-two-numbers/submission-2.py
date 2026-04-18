# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        curr = head
        carry = 0
        while l1 and l2:
            nxt = ListNode(0)
            curr.next = nxt
            curr = curr.next
            curr.val = (l1.val + l2.val + carry) % 10
            if l1.val + l2.val + carry >= 10:
                carry = 1
            else:
                carry = 0
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            nxt = ListNode(0)
            curr.next = nxt
            curr = curr.next
            curr.val = (l1.val + carry) % 10
            if l1.val + carry >= 10:
                carry = 1
            else:
                carry = 0
            l1 = l1.next

        while l2:
            nxt = ListNode(0)
            curr.next = nxt
            curr = curr.next
            curr.val = (l2.val + carry) % 10
            if l2.val + carry >= 10:
                carry = 1
            else:
                carry = 0
            l2 = l2.next
        
        if not l1 and not l2 and carry ==1:
            nxt = ListNode(1)
            curr.next = nxt


        
        return head.next



            






        