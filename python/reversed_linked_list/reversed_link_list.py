# Given two LINKED LISTS [1,4,9,3,7] and [8,2,5,3,6] return 73941 + 63528 = 137469 => LINKED LIST [9,6,4,7,3,1]

def add_two_numbers(l1, l2):
    head = None
    current = None
    carry_over = 0

    while l1 is not None or l2 is not None:
        total_sum = carry_over
        if l1 is not None:
            total_sum += l1.val
            l1 = l1.next
        if l2 is not None:
            total_sum += l2.val
            l2 = l2.next
        node = ListNode(total_sum % 10)
        carry_over = total_sum // 10
        if current is None:
            current = head = node
        else:
            current.next = node
            current = current.next
    if carry_over > 0:
        current.next = ListNode(carry_over)
    return head