"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head:
            last = self.getlast(head)
            return head
        else:
            return None
    
    def getlast(self, p):
        if not p.next:
            if p.child:
                p.next = p.child
                p.child.prev = p
                last = self.getlast(p.child)
                p.child = None
            return p
        
        while p.next:
            if p.child:
                pnext = p.next
                p.next = p.child
                p.child.prev = p
                last = self.getlast(p.child)
                last.next = pnext
                pnext.prev = last
                p.child = None
                p = pnext
            else:
                p = p.next
            
        return p
