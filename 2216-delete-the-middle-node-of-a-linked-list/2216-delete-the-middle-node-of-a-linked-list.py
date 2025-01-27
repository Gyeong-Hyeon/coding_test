# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        node, cnt = head, 1
        while node.next:
            cnt+=1
            node = node.next
        node = head
        for _ in range(1,cnt//2):
            node = node.next
        node.next = node.next.next
        return head