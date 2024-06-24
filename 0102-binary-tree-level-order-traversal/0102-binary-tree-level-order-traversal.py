# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        
        ans, to_visit = [], [root]
        level = 0
        while to_visit:
            vals, node_cnt = [], len(to_visit)
            for _ in range(node_cnt):
                node = to_visit.pop(0)
                vals.append(node.val)
                
                if node.left:
                    to_visit.append(node.left)
                if node.right:
                    to_visit.append(node.right)
            ans.append(vals)
            level+=1
        return ans