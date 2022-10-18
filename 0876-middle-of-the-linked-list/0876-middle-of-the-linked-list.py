# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = head
        cnt = 0
        while n.next:
            n=n.next
            cnt+=1
        cnt = round((cnt/2)+0.1)
        for i in range(cnt+1):
            if i == cnt:
                return head
            head = head.next
        