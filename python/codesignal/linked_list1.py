# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(l, k):
    # create dummy node that is in  "aval" of first node to bypass edge cases
    dummy_node = ListNode(l)
    # create 2 pointers, one at dummy, one at head of initial Linkedlist
    previous, current = dummy_node, l
    
    # as long as the  "current" pointer  didn't reach the end of the list
    while current:
        # save the next node as a variable
        next = current.next
        
        # Must the current node be deleted? (does it match k)
        if current.value == k:
            # bridge from the one before to the one after
            previous.next = next
        else:
            # link previous to current (??? unclear step)
            previous.next = current
            # current of this loop will be previous of the next one
            previous = current
        
        # regardless of if/else output, we will check the next node on next loop
        current = next
    
    # The dummy in "aval" either points at the first node of the list if not k,
    # otherwise it will point at the first occurence of "not-K"
    return dummy_node.next