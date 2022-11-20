# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        node, vals = head, []
        while node:
            vals.append(node.val)
            node = node.next
        node = head
        while vals:
            node.val = vals.pop()
            node = node.next
        return head
