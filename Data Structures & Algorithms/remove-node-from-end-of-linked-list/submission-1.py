# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        h = head
        while h!=None:
            h = h.next
            length+=1


        if length-n==0:
            return head.next

        h2 = head
        for i in range(length):
            if i == length - n - 1:
                h2.next=h2.next.next
                break
            h2 = h2.next
        return head



            
        
       

        