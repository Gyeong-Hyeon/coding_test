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
        """
        1. visit list = [root], prev_node = False
        2. for _ in visit list's length:
            if not prev_node:
                prev_node = visit list.pop(0)
            else:
                node = visit list.pop(0)
                prev_node.next, prev_node = node, node
            if prev_node.left:
                visit list.extend([prev_node's left node, right node])
        5. if not visit list: break the loop
        """
        if not root: return root
        v = [root]
        while v:
            p_node = False
            for _ in range(len(v)):
                if not p_node:
                    p_node = v.pop(0)
                else:
                    node = v.pop(0)
                    p_node.next, p_node = node, node
                if p_node.left:
                    v.extend([p_node.left, p_node.right])
        return root        