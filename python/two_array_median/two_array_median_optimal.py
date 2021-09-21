# https://leetcode.com/problems/median-of-two-sorted-arrays/

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

def find_median(nums1, nums2):
    n = len(nums1) + len(nums2)
    half = n // 2
    
    x,y = nums1, nums2
    
    # trick to make sure x is the shortest one to run binary search on
    if len(y) < len(x):
        x, y = y, x

    # setting pointers of binary search
    left, right = 0, len(x) - 1

    while True:
        i = (left + right) // 2 # x partition from 2 pointers
        j = half - i - 2 # y partition

        x_left_partition = x[i] if i >= 0 else float("-inf")
        x_right_partition = x[i + 1] if (i + 1) < len(x) else float("inf")
        y_left_partition = y[j] if j >= 0 else float("-inf")
        y_right_partition = y[j + 1] if (j+1) < len(y) else float("inf")

        # partition is correct
        if x_left_partition <= y_right_partition and y_left_partition <= x_right_partition:
            # odd
            if n % 2 == 1:
                return min(x_right_partition, y_right_partition)
            # even
            else:
                return (max(x_left_partition, y_left_partition) + min(x_right_partition, y_right_partition)) / 2
        elif x_left_partition > y_right_partition:
            right = i - 1
        else:
            left = i + 1




print(find_median([1,3,8,9,15], [7,11,18,19,21,25])) # should be 11

print(find_median([1,3], [2])) # should be 2
print(find_median([1,2], [3,4])) # should be 2.5
print(find_median([0,0], [0,0])) # should be 0
print(find_median([], [1])) # should be 1
print(find_median([2], [])) # should be 2
print(find_median([1,2,3,4], [1,2,2,3,4])) # should be 2
print(find_median([0,2,4,6], [1,3,5,7])) # should be 3.5
print(find_median([10], [5,6,7,8,11,12,13,14])) # should be 10