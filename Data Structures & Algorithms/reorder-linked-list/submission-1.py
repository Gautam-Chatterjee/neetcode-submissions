# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head 
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
       
        mid = slow.next
        curr = mid
        prev =slow.next= None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        new = ListNode()
        l1 = head
        l2 = prev
        i = 1
        curr = new
        while l1 and l2:
            if i%2 == 0:
                curr.next  = l2
                l2 = l2.next
            else:
                curr.next = l1
                l1 = l1.next
            curr = curr.next
            i+=1
        
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        















