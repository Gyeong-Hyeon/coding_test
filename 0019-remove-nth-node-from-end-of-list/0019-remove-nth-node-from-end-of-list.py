# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        1. Let fast pointer run the linked list by index n-1
        2. When fast pointer arrives nth idx, slow pointer starts
        3. when fast pointer arrive end of the list, slow pointer stops
        4. The total length fast runner run was len(linked list). The first length the fast runner run was n-1. So the second length the fast runner run was len(linked list) - n-1 which is same with the slow pointer run. Therefore, the index where slow pointer points is n-1th from the end of the list.
        5. Make current slow runner.next to slow runner.next.next
        6. return head
        """
        fast, slow = head, head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head