"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        q = [root]
        while q:
            nn = None
            for _ in range(len(q)):
                n = q.pop(0)
                n.next, nn = nn, n
                if n.right:
                    q.extend([n.right, n.left])
        return root