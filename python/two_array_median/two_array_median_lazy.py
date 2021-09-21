# https://leetcode.com/problems/median-of-two-sorted-arrays/

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

def find_median(nums1, nums2):
    nums3 = nums1 + nums2
    nums3.sort()

    n = len(nums3)
    if n % 2 == 0:
        return (nums3[n//2] + nums3[n//2 - 1])/2
    else:
        return nums3[n//2]



print(find_median([1,3], [2])) # should be 2
print(find_median([1,2], [3,4])) # should be 2.5
print(find_median([0,0], [0,0])) # should be 0
print(find_median([], [1])) # should be 1
print(find_median([2], [])) # should be 2
print(find_median([1,2,3,4], [1,2,2,3,4])) # should be 2
print(find_median([0,2,4,6], [1,3,5,7])) # should be 3.5
print(find_median([10], [5,6,7,8,11,12,13,14])) # should be 10