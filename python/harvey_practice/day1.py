[1, -2, 3, 4]

def largest_sum(list):
    right_pointer = len(list) -1
    left_pointer = 0

    highest_sum = 0

    for left_index, left in enumerate(list):
        for i in range(0, len(list)-left_index):
            current_sum = sum(list[left_index:left_index+i+1])
            if  current_sum > highest_sum:
                highest_sum = current_sum
    return highest_sum


def largest_sum2(list):
    right_pointer = 0
    left_pointer = 0

    current_sum = 0

    for i in range(0,len(list)):
        right_pointer += i
        
        if list[right_pointer] < 0 and list[right_pointer] > current_sum:
         left_pointer = right_pointer
            
        current_sum = sum(list[left_pointer:right_pointer+1])


    for left_index, left in enumerate(list):
        for i in range(0, len(list)-left_index):
            current_sum = sum(list[left_index:left_index+i+1])
            if  current_sum > highest_sum:
                highest_sum = current_sum
    return highest_sum


              **
list1 = [1,2,-4,4,5] # 15

                **
list3 = [0, -1] # 7
list4 = [2, -1, 3, 4] # 8
list5 = [2, -9, 3, 4] # 7

print(largest_sum(list1))
print(largest_sum(list3))
print(largest_sum(list4))
print(largest_sum(list5))
