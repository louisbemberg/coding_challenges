# Given two lists [1,4,9,3,7] and [8,2,5,3,6] return 73941 + 63528 = 137469 => [9,6,4,7,3,1]
def add_two_numbers(l1, l2):
    result = int(''.join(reversed([str(i) for i in l1]))) + int(''.join(reversed([str(i) for i in l2])))
    return [int(x) for x in str(result)][::-1]


print(add_two_numbers([1,4,9,3,7], [8,2,5,3,6]))