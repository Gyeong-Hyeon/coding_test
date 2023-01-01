# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Solution 1. find the length of linked list -> return the middle node 
        Solution 2.
         - Move one pointer 2 nodes, the other pointer one node per loop
         - Once the faster pointer reaches the end of the linked list, break the loop
         - Return the node where the slower pointer is pointing
        """
        fast = slow = head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        return slow
