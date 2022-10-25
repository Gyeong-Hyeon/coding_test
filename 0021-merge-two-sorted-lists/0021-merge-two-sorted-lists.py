# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list2 or list1
        ans = move = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                move.next = list1
                move, list1 = list1, list1.next
                continue
            move.next = list2
            move, list2 = move.next, list2.next
        if list1 or list2:
            move.next = list1 if list1 else list2
        return ans.next