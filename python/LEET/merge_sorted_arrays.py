def merge_lists(l1, l2):
    if l1 == [] or l2 == []:
        return l1 + l2

    p1 = 0
    p2 = 0
    count = 0
    l3 = [None] * (len(l1) + len(l2))

    while p1 < len(l1) and p2 < len(l2):
        if l1[p1] <= l2[p2]:
            l3[count] = (l1[p1])
            p1 += 1
        else:
            l3[count] = (l2[p2])
            p2 += 1
        count += 1
    
    # remaining of first, if any:
    while p1 < len(l1):
        l3[count] = l1[p1]
        count += 1
        p1 += 1
    
    while p2 < len(l2):
        l3[count] = l2[p2]
        count += 1
        p2 += 1
    
    return l3


print(merge_lists([1,2,3], []))
print(merge_lists([1,4,6,8], [3,5,7]))
print(merge_lists([1,2,3], [4,5,6]))
print(merge_lists([1,2,3], [1000]))
print(merge_lists([11,12,13], [1]))