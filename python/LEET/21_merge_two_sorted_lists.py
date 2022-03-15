# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # edge cases
        if not list1:
            return list2
        if not list2:
            return list1
        
        # builing a dummy node
        current = ListNode()
        # save the head so we can return it later
        dummy = current

        while list1 or list2:
            if not list1:
                current.next = list2
                list2 = list2.next
            elif not list2:
                current.next = list1
                list1 = list1.next
            elif list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        return dummy.next