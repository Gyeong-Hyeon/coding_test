# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        find the length of linked list by pointer
        """
        p, cnt = head, 0
        while p.next:
            p = p.next
            cnt+=1
        for _ in range(round((cnt/2)+0.1)):
            head = head.next
        return head        