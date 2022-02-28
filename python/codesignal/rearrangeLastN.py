# Intial attempt,
# Only bug is infinite loop as the snake "bits its tail"
# => would have to traverse a third time to set the last value as None
def solution(l, n):
    original_head = l
    new_head = None
    
    total_length = 0
    while l:
        total_length += 1
        l = l.next
        
    # go back to start of list
    l = original_head
    
    count = 0
    while l:
        # are we at the last node before the n group?
        if count == total_length - n - 1:
            print(l.value, 'stahp')
            # head of the new list
            new_head = l
            print('the new head is', new_head.value)
        # are we at the last node of the n group (keeping ifs separate in case of n=1)
        if count == total_length - 1:
            # connect it to the head of the old list
            # l.next = original_head
            print(l.value, 'The end')
        l = l.next
        count += 1

# Other attempt: Two parallel pointers separated by a distance of n
def solution(l, n):
    # keep a reference of the head:
    head = l
    # example input: [1,2,3,4,5], n=3

    # start the 2 pointers at the head
    # [LR0, 1, 2, 3, 4, 5]
    right_pointer = l
    left_pointer = l
    # move the right pointer to make it lead by 3
    for _ in range(n):
        right_pointer = right_pointer.next
    # [L0, 1, 2, R3, 4, 5]

    # guard clause in case length == n 
    if not right_pointer: return l

    # now we move forward until the right pointer reaches the end
    # [0, 1, L2, 3, 4, R5]
    while right_pointer:
        if right_pointer.next == None:
            right_pointer.next = head
            new_head = left_pointer.next
            left_pointer.next = None
            break
        right_pointer = right_pointer.next
        left_pointer = left_pointer.next
    return new_head


# Perfect solution
def solution(l, n):
    if n == 0:
        return l
    front, back = l, l
    for _ in range(n):
        front = front.next
    if not front:
        return l
    while front.next:
        front = front.next
        back = back.next
    out = back.next
    back.next = None
    front.next = l
    return out