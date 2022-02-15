# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None


# return a boolean determining whether a singly linked list is a palindrome.

# Louis's unoptimal version:

def solution(l):
    values = []
    current = l

    while current != None:
        values.append(current.values)
        current = current.next
    
    return values == values[::-1]


# Better solution

def solution(l):
    if l == None:
        return True

    # go to middle of list by having single jump 1 and double jump 2
    # j will end up at the end and i at half.

    i = j = l

    while j.next != None:
        j = j.next.next
        if j == None:
            break
        i = i.next

    # reverse second half of list

    h = i.next
    k = None

    # h is one node right of middle
    # k is the None right of the right node

    # as long as h hasn't reached the end 
    while h != None:

        # add the element to the reversed  right side
        j = h.next
        # connect h to the next reversed node
        h.next = k
        k = h
        i.next = h
        h = j

    # check if second half matches first half

    i = i.next
    
    while i != None:        
        if l.value != i.value: return False      
        i = i.next
        l = l.next
    return True
