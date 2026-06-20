# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = None
        of = 0
        head1 = l1
        head2 = l2
        headans = None
        while head1 != None or head2 != None:
            x = head1.val if head1 else 0
            y = head2.val if head2 else 0
            ne = ListNode((x+y+of) % 10)
            of = (x+y+of) // 10
            if headans is None:
                headans = ne
                ans = headans
            else:
                headans.next = ne
                headans = ne
            head1 = head1.next if head1 else None
            head2 = head2.next if head2 else None
        
        if of != 0 and headans:
            headans.next = ListNode(of)

        return ans
            