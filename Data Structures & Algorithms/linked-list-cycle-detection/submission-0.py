# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        ans = False
        while fast != None and slow != None:
            if slow.next != None:
                slow = slow.next
            if fast.next != None and fast.next.next != None:
                fast = fast.next.next
            else:
                return False
            if slow is fast:
                return True
        
        return ans