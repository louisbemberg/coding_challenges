# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(a, b):
    n1 = ''
    n2 = ''
    
    # Re-create the full number of a
    while a != None:
        n1 += str(a.value).rjust(4, '0')
        a = a.next
    
    # Re-create the full number of b
    while b != None:
        n2 += str(b.value).rjust(4, '0')
        b = b.next
    
    # compute the sum of a + b, turn back into string
    result = str(int(n1) + int(n2))
    print(result)
    
    # if the result is divisible by 4, just slice in chunks of 4
    if len(result) % 4 == 0:
        nodes = [result[i:i+4] for i in range(0, len(result), 4)]
    # if not, also slice in chunks of 4 but from right to left
    else:
        nodes = [result[0:(len(result) % 4)]] + [result[i:i+4] for i in range(len(result) % 4, len(result), 4)]
    print(nodes)
    
    # dummy node trick to be  able to return the head  later
    current = dummy = ListNode(0)
    # create a Listnode based on the result obtained above
    for x in nodes:
        current.next = ListNode(int(''.join(x)))
        current = current.next
    return dummy.next