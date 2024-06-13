# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        vals = []
        for li in lists:
            while li:
                vals.append(li.val)
                li = li.next

        ans = head = ListNode()
        for val in sorted(vals):
            head.next = ListNode(val=val)
            head = head.next
        return ans.next