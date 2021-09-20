# https://leetcode.com/problems/median-of-two-sorted-arrays/

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

def find_median(nums1, nums2):
    import math

    size1 = len(nums1)
    size2 = len(nums2)

    nums3 = [None] * (size1 + size2)
    i, j, k = 0, 0, 0
    
 
    while i < size1 and j < size2:
        # merging operation
        if nums1[i] <= nums2[j]:
            nums3[k] = nums1[i]
            i += 1
        else:
            nums3[k] = nums2[j]
            j += 1
        k += 1

    # append any remaining leftovers
    while i < size1:
        nums3[k] = nums1[i]
        i += 1
        k += 1

    while j < size2:
        nums3[k] = nums2[j]
        j += 1
        k += 1
    
    if (size1 + size2) % 2 == 0:
        return (nums3[int((size1 + size2) / 2)] + nums3[int((size1 + size2) / 2) - 1])/2
    else:
        return nums3[math.floor((size1 + size2) / 2)]


print(find_median([1,3], [2])) # should be 2
print(find_median([1,2], [3,4])) # should be 2.5
print(find_median([0,0], [0,0])) # should be 0
print(find_median([], [1])) # should be 1
print(find_median([2], [])) # should be 2
print(find_median([1,2,3,4], [1,2,2,3,4])) # should be 2
print(find_median([0,2,4,6], [1,3,5,7])) # should be 3.5
print(find_median([10], [5,6,7,8,11,12,13,14])) # should be 10