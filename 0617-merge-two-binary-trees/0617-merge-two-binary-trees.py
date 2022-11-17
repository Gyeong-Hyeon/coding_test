# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        1. If one of the trees is empty, return the other tree. If both are empty, return any one of those.
        2. Else (=means both trees have first node), make a to visit list v = [root1, root2]
        3. Once the nodes are visited, remove those from the list
        4. Change v[0]'s value to sum(v[0]'s val + v[1]'s val)
        5. If v[0] and v[1] both has a left node, append their left nodes to the list so that we can check those at the next loop.
        6. Do 5 for a right node as well.
        7. If v[0] doesn't have a left/right node but v[1] has, change v[1]'s to v[0]'s
        8. Once the list "v" is empty (=there is no more nodes to visit), return tree1     
        """
        if not root1 or not root2: return root2 or root1
        v = [(root1,root2)]
        while v:
            node1, node2 = v.pop()
            node1.val+=node2.val
            if node1.left and node2.left:
                v.append((node1.left,node2.left))
            if node1.right and node2.right:
                v.append((node1.right,node2.right))
            if not node1.left and node2.left:
                node1.left = node2.left
            if not node1.right and node2.right:
                node1.right = node2.right
        return root1