# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_val, q_val, parent = p.val, q.val, root
        while parent:
            parent_val = parent.val
            if p_val > parent_val and q_val > parent_val:
                parent = parent.right
            elif p_val < parent_val and q_val < parent_val:
                parent = parent.left
            else:
                return parent