# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        to_visit = [(p,q)]
        while to_visit:
            p, q = to_visit.pop()
            if p and q and p.val == q.val:
                to_visit.extend([
                    (p.left, q.left),
                    (p.right, q.right)
                ])
            elif p or q:
                return False
        return True