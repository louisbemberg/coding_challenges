# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(a, b):
    n1 = ''
    n2 = ''
    
    while a != None:
        n1 += str(a.value).rjust(4, '0')
        a = a.next
    
    while b != None:
        n2 += str(b.value).rjust(4, '0')
        b = b.next
        
    result = str(int(n1) + int(n2))
    print(result)
    nodes = [reversed(result)[i:i+4] for i in range(0, len(result), 4)]
    print(nodes)
    
    current = dummy = ListNode(0)
    for x in nodes:
        current.next = ListNode(int(x))
        current = current.next
    return dummy.next