"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ans = None
        cur = head
        if not head:
            return None
        while cur != None:
            x = Node(cur.val)
            x.to = cur
            cur.to = x
            cur = cur.next
        
        original, ne = head, head.to

        while ne:
            ne.next = ne.to.next.to if ne.to.next else None
            ne.random = ne.to.random.to if ne.to.random else None
            x = ne.random.val if ne.random else 'none'
            ne = ne.next
            
        
        return head.to
            