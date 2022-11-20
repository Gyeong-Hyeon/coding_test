# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Make a new linked list
        1. list1.val < list2.val: node.val = list1.val, move node and list1 to next
        2. else: node.val = list2.val, move node and list2 to next
        3. If list1 or list2 reached to each's last node, make node.next.next to the other linked list
        """
        if not list1 or not list2: return list2 or list1
        merged = node = ListNode()
        while list1 or list2:
            if list1.val < list2.val:
                node.next = list1
                if not list1.next:
                    node.next.next = list2
                    break
                else:
                    list1 = list1.next
            else:
                node.next = list2
                if not list2.next:
                    node.next.next = list1
                    break
                else:
                    list2 = list2.next
            node = node.next
        return merged.next        