# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l,lmn=head,head
        for _ in range(n):
            l=l.next
        if not l:
            return head.next
        while l.next:
            l=l.next
            lmn=lmn.next
        lmn.next = lmn.next.next
        return head