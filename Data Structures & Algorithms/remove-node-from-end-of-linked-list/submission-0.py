# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        cnt = 0
        if not head:
            return None
        while cur != None:
            cnt += 1
            cur = cur.next
        
        tar = cnt - n
        if tar == 0:
            return head.next
        cur = head
        prev = head
        nxt = head.next
        for i in range(tar):
            prev = cur
            nxt = nxt.next
            cur = cur.next
            
        if nxt is None:
            prev.next = None
        else:
            prev.next = nxt
        return head
