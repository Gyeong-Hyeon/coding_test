# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        vals, node = [], head
        while node:
            vals.append(node.val)
            node = node.next

        length, mid, new_node = len(vals)-1, len(vals)//2, head
        for i in range(mid):
            new_node.val, new_node.next.val = vals[i], vals[length-i]
            new_node = new_node.next.next
        if new_node:
            new_node.val = vals[mid]