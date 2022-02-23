# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

# a b c d E F G H
# d c b a E F G H
def solution(l, k):
    # set dummy variable at the very left of the list
    dummy = ListNode(0)
    # connect to the beginning of the input list (note that it prob won't be the beginning of the output list)
    dummy.next = l
    # we always want to keep track of the node that will get connected to the next flipped group. we call it before_group
    before_group = dummy
    
    # The loop will break as soon as the next kth node is null. This happens either when the end of the list is reached, or when the remainder of nodes is not divisible by k. 
    while True:
        # calling a function to find the "end" of the current group (which will become the beginning)
        kth_node = getKthNode(before_group, k)
        # loop breaking logic, explained above
        if not kth_node: break
        # similar logic to before_group, we track the node that comes right after the group in question
        after_group = kth_node.next
        
        # we set pointers to flip the current group
        previous, current = kth_node.next, before_group.next
        # stop before we reached the end of the group
        while current != after_group:
            # temporary variable
            nxt = current.next
            # the next was on the right, it's now on the left
            current.next = previous
            # shift previous 1 to the right
            previous = current
            # shift current 1 to the right
            current = nxt
        
        # the head of the original group is now the tail, let's track it
        old_head_now_tail = before_group.next
        # we connect the end of the previous group with the beginning of the modified group
        before_group.next = kth_node
        # the new "before group" is the node right before the next group. 
        before_group = old_head_now_tail
    
    # using the initial dummy to retrieve the head of the final product 
    return dummy.next   
        
        
def getKthNode(curr, k):
    while curr and k > 0:
        curr = curr.next
        k -= 1
    return curr


# returns a linked list with its first k elements reversed 
def reverse_first_k_elements(l, k):
    flipped_tail = l
    previous, current = None, l
    amt
    for i in range(k):
        nxt = current.next
        current.next = previous
        previous = current
        current = nxt
    l.next = nxt
    
    return previous