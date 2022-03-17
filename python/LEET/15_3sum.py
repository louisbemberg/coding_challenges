# absolute worst solution: triple loop n^3 brute force
# my own solution
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         triplets = []
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 for k in range(len(nums)):
#                     if nums[i]+nums[j]+nums[k] == 0:
#                         triplets.append([nums[i],nums[j],nums[k]])
        
#         # doesn't work as it doesn't remove duplicates and  it's awfully slow
#         return triplets


# optimal solution
class Solution:
    def threeSum(self, nums):
        # variable to inject the triplets
        output = []
        # recall that sort is destructive while sorted() returns a copy
        nums.sort()

        # first traversal of the array, fixing x
        for index, number in enumerate(nums):
            print('x is currently', f"index: {index}, number: {number}")
            # recall the array is sorted, so we only care about
            # the first edition of a series of numbers as X (note that the rest can still be Y or Z)
            if index > 0 and number == nums[index - 1]:
                print('skipping')
                continue
            
            # set the left and right pointers for Y and Z (X is fixed)
            left, right = index + 1, len(nums) - 1
            # shrink window according to conditions
            while left < right:
                triple_sum = number + nums[left] + nums[right]
                # if the sum is too large, remove a large number
                if triple_sum > 0:
                    right -= 1
                # if the sum is too small, remove the most negative
                elif triple_sum < 0:
                    left += 1
                # otherwise, the sum was correct! yay!
                else:
                    # add the triplet to the output
                    # note that uniqueness is  guaranteed by number being on the left and L/R pointers
                    output.append([number, nums[left], nums[right]])
                    # once appended, shift the pointer to the left
                    left += 1
                    # keep shifting the left pointer until it finds a new number (but doesnt overtake right)
                    while nums[left] == nums[left-1] and left <  right:
                        left += 1
        return output



            

        # key idea: 
        # imagine you fix one of the numbers, say x
        # now you need to figure out a way to make the other two the negative of it!
        # => problem boils down to two-sum with a moving third element

solu = Solution()

print(solu.threeSum([-3, -2, -2, -1, 0, 1, 2, 4]))