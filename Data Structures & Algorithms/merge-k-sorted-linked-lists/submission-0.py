# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        tmp = False
        pq = []
        k = len(lists)
        for i in range(k):
            if lists[i]:
                heapq.heappush(pq, (lists[i].val, i))
        ans = None
        cur = None
        while pq:
            x, i = heapq.heappop(pq)
            if not tmp:
                ans = ListNode(x)
                cur = ans
                tmp = True
            else:
                cur.next = ListNode(x)
                cur = cur.next
            
            lists[i] = lists[i].next
            if lists[i]:
                heapq.heappush(pq, (lists[i].val, i))
        
        return ans


             