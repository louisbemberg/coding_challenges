# https://leetcode.com/problems/median-of-two-sorted-arrays/

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).
import statistics

def find_median(nums1, nums2):
    size1 = len(nums1)
    size2 = len(nums2)

    if size1 + size2 <= 4:
        return statistics.median(nums1 + nums2)

    nums3 = []
    i, j = 0, 0
    
    while i < size1 and j < size2:
        # merging operation
        if nums1[i] <= nums2[j]:
            nums3.append(nums1[i])
            i += 1
        else:
            nums3.append(nums2[j])
            j += 1

        # stop the merging as soon as we have the first half + 1 of the numbers
        if len(nums3) > (size1 + size2)/2: break
    
    # implementation of median for odd/even numbers
    return sum(nums3[-2:])/2 if (size1+size2 % 2 == 0) else nums3[-1]


print(find_median([1,3], [2]))
print(find_median([1,2], [3,4]))
print(find_median([0,0], [0,0]))
print(find_median([], [1]))
print(find_median([2], []))
print(find_median([1,2,3,4], [1,2,2,3,4]))
print(find_median([0,2,4,6], [1,3,5,7]))
print(find_median([10], [5,6,7,8,11,12,13,14]))