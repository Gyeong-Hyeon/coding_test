# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list2 or list1
        node1, node2 = (list1, list2) if list1.val < list2.val else (list2, list1)
        head = node1
        while node1 and node2:
            while node1.next and node1.next.val < node2.val:
                node1 = node1.next
            node1.next, node2 = node2, node1.next
            node1 = node1.next
        return head