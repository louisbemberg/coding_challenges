# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # edge case: if one node or no nodes
        if not head or not head.next:
            return head
        
        
        current = head
        previous = None
        next = current.next

        while current:
            # saving the next node to the right so we can jump to it after
            next = current.next
            # the next is now to the left instead of the right
            current.next = previous
            # we can now shift things to the left:
            previous = current
            current = next
        
        return previous