# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def size(head):
            total = 0
            root = head
            while root:
                total += 1
                root = root.next
            return total
        
        list_size = size(head)
       # if 0th element then just return head.next
        if n == list_size:
            return head.next
        # else traverse to the node at the new index
		# traack and update previours node's next node
        newIndex = list_size - n
        cur, prev = head, None
        while cur and newIndex > 0:
            newIndex -= 1
            prev = cur
            cur = cur.next
        prev.next = prev.next.next

        return head
        