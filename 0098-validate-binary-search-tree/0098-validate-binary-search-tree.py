# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isBST(node, mini, maxi):
            if not node:
                return True
            if mini != None and node.val <= mini:
                return False
            if maxi != None and node.val >= maxi:
                return False
            return isBST(node.left, mini, node.val) and isBST(node.right, node.val, maxi)
        return isBST(root.left, None, root.val) and isBST(root.right, root.val, None)