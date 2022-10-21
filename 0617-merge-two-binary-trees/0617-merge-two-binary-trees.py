# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 or not root2:
            return root2 or root1
        s = [(root1, root2)]
        while s:
            r1, r2 = s.pop()
            if not r2:
                continue
            r1.val+= r2.val
            if r1.left:
                s.append((r1.left,r2.left))
            if r1.right:
                s.append((r1.right,r2.right))
            if not r1.left:
                r1.left = r2.left
            if not r1.right:
                r1.right = r2.right
        return root1   