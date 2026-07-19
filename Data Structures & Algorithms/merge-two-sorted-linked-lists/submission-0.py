# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        if not list1:
            return list2
        if not list2:
            return list1
        ans = None
        anst = None
        while head1 and head2:
            v1, v2 = head1.val, head2.val
            print(v1, v2)
            if v1 < v2:
                if ans:
                    anst.next = head1
                    anst = anst.next
                    
                else:
                    ans = head1
                    anst = head1
                head1 = head1.next
            else:
                if ans:
                    anst.next = head2
                    anst = anst.next
                    
                else:
                    ans = head2 
                    anst = head2

                head2 = head2.next
            
        if head1:
            anst.next = head1

        if head2:
            anst.next = head2
        return ans
