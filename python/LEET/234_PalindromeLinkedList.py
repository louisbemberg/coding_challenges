# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # edge cases
        if not head: 
            return True
        
        if not head.next:
            return True
        
        # one approach: store values in a list, but not very efficient
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        
        # lazy, checks the entire array
        # return vals == vals[::-1]

        # slightly more efficient
        left, right = 0, len(vals - 1)

        while left <= right:
            if vals[left] != vals[right]:
                return False
            left += 1
            right -= 1
            return True

    
    # OPTIMAL STRATEGY
    # Create a slow and fast pointer
    # slow pointer jumps 1 while fast jumps 2
    # once fast reaches the end, slow is at the half of the list
    # then, we can start comparing the first half to the later half
    # the issue? how can we make "fast" go backwards?
    # => we will reverse the linked list from the middle onwards.

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        fast, slow = head, head

        # fast gets to the end,  slow gets to half
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse the  second half of the LL, starting from slow
        previous = None
        while slow:
            next = slow.next
            slow.next = previous
            previous = slow
            slow = next

        # now we can start at each extremity and check
        left, right = head, previous

        # right will be the deciding factor
        # remember that we reversed the LL and made the middle point to null

        while right:
            if right.val != left.val:
                return False
            right = right.next
            left = left.next
        return True



